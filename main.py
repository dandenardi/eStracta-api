from flask import Flask, request
from flask_cors import CORS
from flask_restx import Api, Resource, Namespace, fields

app = Flask(__name__)
CORS(app)
api = Api(app, doc='/api')

eStracta = Namespace('companies', description='eStracta API for companies')

company_model = api.model('Company', {

    'CNPJ': fields.String(required=True, description='Codigo de pessoa juridica da empresa'),
    'nome_razao': fields.String(required=True, description='Nome razao'),
    'nome_fantasia': fields.String(required=True, description='Nome fantasia'),
    'CNAE': fields.List(fields.String, required=True, description='Classificacao Nacional de Atividades Economicas'),

})


companies_data = [{'CNPJ': '62582364550213', 'nome_razao': 'fAFZXyolFt', 'nome_fantasia': 'LWdEPhoiQF', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '25383094559265', 'nome_razao': 'UBxOJwBIwP',
                      'nome_fantasia': 'QCzeIcQMyv', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '72674673246947', 'nome_razao': 'cyRnBWVtmU',
                      'nome_fantasia': 'qaocmKzAYs', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '61735816268186', 'nome_razao': 'aedEHcIgbz',
                      'nome_fantasia': 'jbPdzGidFZ', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '65806093117751', 'nome_razao': 'PRUKnZjpyp',
                      'nome_fantasia': 'xEWpdnvouE', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '86211936891415', 'nome_razao': 'nyyhtIybht',
                      'nome_fantasia': 'xhBzHGlFBJ', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '76281180159829', 'nome_razao': 'qKmwfwVUVX',
                      'nome_fantasia': 'ukITPPKFzn', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '02653350513779', 'nome_razao': 'xKkMlLihdx',
                      'nome_fantasia': 'bSOrgyPLko', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {
                      'CNPJ': '03545377230682', 'nome_razao': 'WENVRRZmyi', 'nome_fantasia': 'qygfNeWZyh', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '81762731214826', 'nome_razao': 'THHZrornAX',
                      'nome_fantasia': 'gerkiJzjWy', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '41074358381336', 'nome_razao': 'QYOAPuneOm',
                      'nome_fantasia': 'NDwHVLUBjI', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '56431294484531', 'nome_razao': 'tmaZumaPiI',
                      'nome_fantasia': 'csIlpaHVEf', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '83577779391075', 'nome_razao': 'zrcphmfDww',
                      'nome_fantasia': 'TIjSaSNYlh', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '41722988186371', 'nome_razao': 'sCUPaViUrm',
                      'nome_fantasia': 'poRYddsefV', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '09436059767180', 'nome_razao': 'UyTBdxuciv',
                      'nome_fantasia': 'ThZUDeFCSk', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '31058789468128', 'nome_razao': 'qWTGQYzvxa',
                      'nome_fantasia': 'NSBwQIBGBr', 'CNAE': ['6202-3', '6209-1', '6204-0']},

                  {'CNPJ': '75199765025212', 'nome_razao': 'lIndDPaPCN',
                      'nome_fantasia': 'HpfgHSZSbd', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '77439017968318', 'nome_razao': 'ejnMeJzCav',
                   'nome_fantasia': 'FgmAfmSLqV', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '56520933149140', 'nome_razao': 'COgITvNBpO',
                      'nome_fantasia': 'JWmJuzhBGZ', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '51035139739034', 'nome_razao': 'iXsLtxRYxD',
                      'nome_fantasia': 'NHertIXWMw', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '30056235449322', 'nome_razao': 'PWQCVWuBnw',
                      'nome_fantasia': 'MDmyFtHuTN', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '85361835695935', 'nome_razao': 'CoVasvucHq',
                      'nome_fantasia': 'TzxufxhZDf', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '21927164930986', 'nome_razao': 'ORgNiDXIzU', 'nome_fantasia': 'cxKyCjCUgR', 'CNAE': [
                      '6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '07931887100172', 'nome_razao': 'CWhbrCfhFF',
                      'nome_fantasia': 'jtGalChYRY', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '34428498866105', 'nome_razao': 'IPfLJLfTDv',
                      'nome_fantasia': 'qlRpAyDRkz', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '81562473550189', 'nome_razao': 'bGcJGOZGxj',
                      'nome_fantasia': 'GXdiENrRSD', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '79985359461715', 'nome_razao': 'JTlosELuau',
                      'nome_fantasia': 'YLIlxBFyqB', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '18577311136848', 'nome_razao': 'jtkuoLagMg',
                      'nome_fantasia': 'JIKouEuxVW', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '47842020305218', 'nome_razao': 'PjbZEHEWhj',
                      'nome_fantasia': 'XyrCsREujg', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '97717724122850', 'nome_razao': 'CavTPrfsaf',
                      'nome_fantasia': 'acefZQlppM', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '34474572353767', 'nome_razao': 'sNnAnIRQqq', 'nome_fantasia': 'QeQYIjJarB', 'CNAE': [
                      '6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '14130716854799', 'nome_razao': 'fWAItdOcyB',
                      'nome_fantasia': 'mbKuAIkmbq', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '55443261283636', 'nome_razao': 'ThvRaTJgSN',
                      'nome_fantasia': 'KntkoNMoUX', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '67793325658339', 'nome_razao': 'uAIBjlwhNv', 'nome_fantasia': 'QszjzZrtlx', 'CNAE': [
                      '6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '71963571780254', 'nome_razao': 'ULnJgGZmEt',
                      'nome_fantasia': 'kHdDrPwPSw', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '26437616607438', 'nome_razao': 'wkeSyTMuZv',
                      'nome_fantasia': 'PIWAWvBeFT', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '76939977510478', 'nome_razao': 'HLPCKRNCcc',
                      'nome_fantasia': 'GiThyiUbRF', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '88998225592433', 'nome_razao': 'bUIaFWeMCw',
                      'nome_fantasia': 'DTqYOduFds', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '43960753590837', 'nome_razao': 'GpnGdroRWc',
                      'nome_fantasia': 'GzvlyTDIQR', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '24980080189776', 'nome_razao': 'hYWrryEXXM',
                      'nome_fantasia': 'hstyxjllmW', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '10261322600544', 'nome_razao': 'EAWteRoPss',
                      'nome_fantasia': 'IlxUnjOvSC', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '29918490503467', 'nome_razao': 'SwTshnnOYN',
                      'nome_fantasia': 'oPWnqXuUok', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '72591053822741', 'nome_razao': 'ozkQqYuAzJ',
                      'nome_fantasia': 'csdrdxXZcH', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '77085272611811', 'nome_razao': 'GBMLnlwSIK',
                      'nome_fantasia': 'ILcRBmWUpN', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '74122759400992', 'nome_razao': 'ZtRyQaSPbr',
                      'nome_fantasia': 'MMsaVuYwsj', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '17511826997322', 'nome_razao': 'iLYVHHkwdS',
                      'nome_fantasia': 'PybxEHaCpD', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '07961996421694', 'nome_razao': 'rjWFLQkoWi',
                      'nome_fantasia': 'ipvwamiRqi', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '95929896364473', 'nome_razao': 'JUUOkPxhLY',
                      'nome_fantasia': 'dZVNRYhnIG', 'CNAE': ['6202-3', '6209-1', '6204-0']},
                  {'CNPJ': '09453558232770', 'nome_razao': 'pzoLjenDWo', 'nome_fantasia': 'VYUokfFLtI', 'CNAE': ['6202-3', '6209-1', '6204-0']}]


@eStracta.route('/companies')
class AllCompanies(Resource):
    @eStracta.marshal_list_with(company_model)
    def get(self):
        '''
        Lists all companies
        '''

        start = int(request.args.get('start', 0))
        limit = int(request.args.get('limit', 25))
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

    @eStracta.expect(company_model)
    @eStracta.marshal_with(company_model)
    def post(self):
        """
            Create a new company
        """
        data = request.json

        cnae_codes = data.get('CNAE', [])

        new_company = {'CNPJ': data['CNPJ'], 'nome_razao': data['nome_razao'],
                       'nome_fantasia': data['nome_fantasia'], 'CNAE': cnae_codes}

        companies_data.append(new_company)


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

    @eStracta.expect(company_model)
    @eStracta.marshal_with(company_model)
    def delete(self, cnpj):
        """ Based on CNPJ, delete the corresponding company"""

        global companies_data
        companies_data = [c for c in companies_data if c['CNPJ'] != cnpj]
        return {"message": f"Company with CNPJ {cnpj} deleted successfully"}, 200

    @eStracta.expect(company_model)
    @eStracta.marshal_with(company_model)
    def put(self, cnpj):
        """
            Updating having as base the company's CNPJ
        """
        data = request.json

        company = next((c for c in companies_data if c['CNPJ'] == cnpj), None)

        if not company:
            eStracta.abort(404, f"Company with CNPJ {cnpj} couldn't be found")

        if 'nome_fantasia' in data:
            company['nome_fantasia'] = data['nome_fantasia']

        if 'CNAE' in data:
            new_cnae_codes = data['CNAE']
            existing_cnae_codes = company.get('CNAE', [])
            updated_cnae_codes = list(
                set(existing_cnae_codes + new_cnae_codes))
            company['CNAE'] = updated_cnae_codes

        return company


api.add_namespace(eStracta, path='/api/v1')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
