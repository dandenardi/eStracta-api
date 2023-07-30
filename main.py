from flask import Flask, request
from flask_restx import Api, Resource, Namespace, fields

app = Flask(__name__)
api = Api(app, doc='/api')

eStracta = Namespace('companies', description='eStracta API for companies')

company_model = api.model('Company', {

    'CNPJ': fields.String(required=True, description='Codigo de pessoa juridica da empresa'),
    'nome_razao': fields.String(required=True, description='Nome razao'),
    'nome_fantasia': fields.String(required=True, description='Nome fantasia'),
    'CNAE': fields.List(fields.String, required=True, description='Classificacao Nacional de Atividades Economicas'),

})


companies_data = [
    {'CNPJ': '40034183000180',
        'nome_razao': 'Joao da Silva ME', 'nome_fantasia': 'Novo Site - Websites responsivos', 'CNAE': ['6201-5']},
    {'CNPJ': '21918100000171',
        'nome_razao': 'Estracta Tecnologia LTDA', 'nome_fantasia': 'Estracta Tecnologia LTDA', 'CNAE': ['6202-3', '6209-1', '6204-0']},

]


@eStracta.route('/companies')
class AllCompanies(Resource):
    @eStracta.marshal_list_with(company_model)
    def get(self):
        '''
        Lists all companies
        '''

        start = int(request.args.get('start', 0))
        limit = int(request.args.get('limit', 10))
        sort = request.args.get('sort', 'CNPJ')
        dir = request.args.get('dir', 'asc')

        sorted_companies = sorted(
            companies_data, key=lambda x: x[sort], reverse=(dir.lower() == 'desc'))

        paginated_companies = sorted_companies[start:start + limit]

        return paginated_companies


@eStracta.route('/')
class AllCompaniesBase(Resource):
    def get(self):
        """Lists all companies in default configuration."""

        return companies_data


eStracta.add_resource(AllCompaniesBase, '/')


@eStracta.route('/company/<string:cnpj>')
class Company(Resource):
    @eStracta.marshal_with(company_model)
    def get(self, cnpj):
        """
            Returns detailed information from a company, based its CNPJ.
        """
        company = next((c for c in companies_data if c['CNPJ'] == cnpj), None)

        if company:
            return company

        eStracta.abort(404, f"Company with ID {id} does not exist")


def delete(self, cnpj):
    """ Based on CNPJ, delete the corresponding company"""

    global companies_data
    companies_data = [c for c in companies_data if c['CNJP'] != cnpj]
    return {"message": f"Company with CNPJ {cnpj} deleted successfully"}, 200


@eStracta.expect(company_model)
@eStracta.marshal_with(company_model)
def post(self):
    """
        Create a new company
    """
    data = request.json

    cnae_codes = data.get('CNAE', [])

    new_company = {'id': len(
        companies_data) + 1, 'CNPJ': data['cnpj'], 'nome_razao': data['nome_razao'], 'nome_fantasia': data['nome_fantasia'], 'CNAE': cnae_codes}

    companies_data.append(new_company)


@eStracta.expect(company_model)
@eStracta.marshal_with(company_model)
def put(self, id):
    """
        Updating having as base the company's ID
    """
    data = request.json

    company = next((c for c in companies_data if c['id'] == id), None)

    if not company:
        eStracta.abort(404, f"Company with ID {id} couldn't be found")

    if 'nome_fantasia' in data:
        company['nome_fantasia'] = data['nome_fantasia']

    if 'CNAE' in data:
        new_cnae_codes = data['CNAE']
        existing_cnae_codes = company.get('CNAE', [])
        updated_cnae_codes = list(set(existing_cnae_codes + new_cnae_codes))
        company['CNAE'] = updated_cnae_codes

    return company


api.add_namespace(eStracta, path='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
