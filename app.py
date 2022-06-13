import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.title = 'dosage optimisation'
app.description = """dosage optimisation app"""
server = app.server

app.index_string = """<!DOCTYPE html>
<html>
    <head>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id="></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', '');
</script>

 {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <meta property="og:type" content="article">
        <meta property="og:title" content="cement"">
        <meta property="og:site_name" content="https://www.cem-quality.net">
        <meta property="og:url" content="https://www.cem-quality.net">
        <meta property="article:published_time" content="2021-10-28">
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""
