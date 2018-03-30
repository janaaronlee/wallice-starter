def get(request):
    return {'hello': request.uri_params['name']}
