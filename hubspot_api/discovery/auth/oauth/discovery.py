import hubspot_api.codegen.auth.oauth as oauth


class Discovery:
    def default_api(self):
        configuration = oauth.Configuration()
        configuration.api_key['hapikey'] = '220a09eb-7f6c-4012-99f7-7c7f0692f18a'

        return oauth.DefaultApi(oauth.ApiClient(configuration))
