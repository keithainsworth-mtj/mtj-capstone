from nicegui import ui

@ui.page('/')
def index():
    ui.label('👋 Welcome to the MTJ Capstone App!')
    ui.label('This app demonstrates AI-powered metadata profiling using Open Payments data.')
    ui.label('More features coming soon...')

ui.run()