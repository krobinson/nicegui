from nicegui import ui

from ..documentation_tools import text_demo


def main_demo() -> None:
    from random import random

    chart = ui.chart({
        'title': False,
        'chart': {'type': 'bar'},
        'xAxis': {'categories': ['A', 'B']},
        'series': [
            {'name': 'Alpha', 'data': [0.1, 0.2]},
            {'name': 'Beta', 'data': [0.3, 0.4]},
        ],
    }).classes('w-full h-64')

    def update():
        chart.options['series'][0]['data'][0] = random()
        chart.update()

    ui.button('Update', on_click=update)


def more() -> None:
    @text_demo('Chart with extra dependencies', '''
        To use a chart type that is not included in the default dependencies, you can specify extra dependencies.
        This demo shows a solid gauge chart.
    ''')
    def extra_dependencies() -> None:
        ui.chart({
            'title': False,
            'chart': {'type': 'solidgauge'},
            'yAxis': {
                'min': 0,
                'max': 1,
            },
            'series': [
                {'data': [0.42]},
            ],
        }, extras=['solid-gauge']).classes('w-full h-64')

    @text_demo('Chart with point dragging enabled', '''
        This chart allows data manipulation by dragging the series points. Data can be read via the on_change callback.
    ''')
    def drag() -> None:
        ui.chart({
            'title': False,
            'plotOptions': {
                'series': {
                    'stickyTracking': False,
                    'dragDrop': {'draggableX': True, 'draggableY': True, 'dragPrecisionX': 1, 'dragPrecisionY': 1},
                },
            },
            'series': [
                {'name': 'A', 'data': [[20, 10], [30, 20], [40, 30]]},
                {'name': 'B', 'data': [[50, 40], [60, 50], [70, 60]]},
            ],
        },  extras=['draggable-points'],
            on_change=lambda e: ui.notify(f'The value changed to {e}.')
        ).classes('w-full h-64')
