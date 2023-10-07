from sanic.views import HTTPMethodView
from sanic_ext import render


class HomeController(HTTPMethodView):
    """Base controller. Manages the display of the main dashboard.
        TODO: Instantiate analysis models using data from csv repositories
        TODO: Pass model data into templates
        TODO: Return rendered page *or*, define multiple HTTP methods & parameters below
        for use with HTMX. This way, we can return the page skeleton with this GET
        method, and the visualizations and tables via discrete HTMX POST methods.
    """
    async def get(self, request):

        return await render('home.html', context={}, status=200)

    async def post(self, request):
        return await render('components/confirm.html', context={'message': 'Yep, this is a POST response'}, status=200)
