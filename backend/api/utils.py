from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def response_pdf(data):
    pdfmetrics.registerFont(
            TTFont('Handicraft', 'data/Handicraft.ttf', 'UTF-8'))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ('attachment; '
                                        'filename="shopping_list.pdf"')
    page = canvas.Canvas(response)
    page.setFont('Handicraft', size=24)
    page.drawString(200, 800, 'Список покупок')
    page.setFont('Handicraft', size=16)
    height = 750
    for i, (name, data) in enumerate(data.items(), 1):
        page.drawString(75, height, (f'{i}. {name} - {data["amount"]} '
                                        f'{data["measurement_unit"]}'))
        height -= 25
    page.showPage()
    page.save()
    return response
