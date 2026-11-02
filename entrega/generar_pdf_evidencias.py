import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def create_evidence_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=1,
        spaceAfter=15
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#2563EB'),
        alignment=1,
        spaceAfter=25
    )

    meta_style = ParagraphStyle(
        'MetaText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#1F2937'),
        alignment=1
    )

    h1_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=10,
        spaceAfter=8,
        keepWithNext=True
    )

    desc_style = ParagraphStyle(
        'DescText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#374151'),
        spaceAfter=10
    )

    box_text_style = ParagraphStyle(
        'BoxText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#6B7280'),
        alignment=1
    )

    story = []

    # ==================== PORTADA (PÁGINA 1) ====================
    story.append(Spacer(1, 40))
    story.append(Paragraph("UNIDAD CENTRAL DEL VALLE DEL CAUCA - UCEVA", subtitle_style))
    story.append(Paragraph("FACULTAD DE INGENIERÍA - PROGRAMACIÓN MÓVIL", meta_style))
    story.append(Spacer(1, 30))
    story.append(Paragraph("TALLER 1: DISTRIBUCIÓN DE APK CON FIREBASE APP DISTRIBUTION", title_style))
    story.append(Paragraph("DOCUMENTO UNIFICADO DE EVIDENCIAS Y BITÁCORA DE QA", subtitle_style))
    story.append(Spacer(1, 40))

    info_data = [
        [Paragraph("<b>Estudiante:</b>", meta_style), Paragraph("Johan Eliu Salgado Castro", meta_style)],
        [Paragraph("<b>Asignatura:</b>", meta_style), Paragraph("Programación Móvil", meta_style)],
        [Paragraph("<b>Application ID:</b>", meta_style), Paragraph("<code>com.johansalgado.taller_app_distribution</code>", meta_style)],
        [Paragraph("<b>Grupo QA Firebase:</b>", meta_style), Paragraph("QA_Clase", meta_style)],
        [Paragraph("<b>Tester Evaluador:</b>", meta_style), Paragraph("dduran@uceva.edu.co", meta_style)],
        [Paragraph("<b>Repositorio GitHub:</b>", meta_style), Paragraph("<font color='#2563EB'><u>https://github.com/Johan-salgado/movil-taller1-app-distribution.git</u></font>", meta_style)],
        [Paragraph("<b>Fecha límite:</b>", meta_style), Paragraph("Lunes 2 de noviembre de 2026, 23:59", meta_style)],
    ]

    info_table = Table(info_data, colWidths=[150, 360])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F3F4F6')),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#3B82F6')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E5E7EB')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(info_table)

    story.append(Spacer(1, 30))
    story.append(Paragraph("<b>Instrucciones de consolidación:</b> Este documento contiene las secciones numeradas y estandarizadas requeridas por la guía. Cada sección cuenta con su marco delimitado para incrustar las capturas de pantalla tomadas durante el proceso de pruebas.", desc_style))

    story.append(PageBreak())

    def make_placeholder_box(text, height=220):
        content = [
            Spacer(1, (height / 2) - 20),
            Paragraph(f"<b>[ PEGAR CAPTURA AQUÍ ]</b><br/>{text}", box_text_style),
            Spacer(1, (height / 2) - 20),
        ]
        box_table = Table([[content]], colWidths=[520], rowHeights=[height])
        box_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F9FAFB')),
            ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#9CA3AF')),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        return box_table

    # ==================== SECCIÓN 1: RELEASES ====================
    story.append(Paragraph("1. Panel de Releases en Firebase App Distribution", h1_style))
    story.append(Paragraph("Captura del panel de Firebase App Distribution donde se evidencien los releases subidos (versión 1.0.0 y versión 1.0.1) con sus números de versión legibles.", desc_style))
    story.append(make_placeholder_box("Captura de pantalla del panel Releases (Firebase Console)", 220))
    story.append(Spacer(1, 15))

    # ==================== SECCIÓN 2: TESTERS ====================
    story.append(Paragraph("2. Grupo de Testers y Asignación de Evaluador", h1_style))
    story.append(Paragraph("Captura de la sección 'Testers y grupos' donde se aprecie el grupo <b>QA_Clase</b> y el correo del evaluador agregado: <b>dduran@uceva.edu.co</b>.", desc_style))
    story.append(make_placeholder_box("Captura de pantalla de Testers & Groups mostrando dduran@uceva.edu.co en QA_Clase", 220))

    story.append(PageBreak())

    # ==================== SECCIÓN 3: CORREO INVITACIÓN ====================
    story.append(Paragraph("3. Correo de Invitación Recibido por el Tester", h1_style))
    story.append(Paragraph("Captura del correo electrónico de invitación enviado por Firebase App Distribution para probar la aplicación móvil.", desc_style))
    story.append(make_placeholder_box("Captura del correo de invitación recibido (App Distribution)", 220))
    story.append(Spacer(1, 15))

    # ==================== SECCIÓN 4: APP INSTALADA EN DISPOSITIVO FÍSICO ====================
    story.append(Paragraph("4. Aplicación Instalada y Abierta en Dispositivo Físico", h1_style))
    story.append(Paragraph("Captura o fotografía del dispositivo móvil real con la aplicación instalada e iniciada mostrando la pantalla inicial con la <b>Versión 1.0.0</b>.", desc_style))
    story.append(make_placeholder_box("Foto/Captura de la app v1.0.0 instalada y abierta en el dispositivo físico", 220))

    story.append(PageBreak())

    # ==================== SECCIÓN 5: EVIDENCIA ACTUALIZACIÓN ANTES / DESPUÉS ====================
    story.append(Paragraph("5. Evidencia de Flujo de Actualización (Antes / Después: 1.0.0 → 1.0.1)", h1_style))
    story.append(Paragraph("Comparativa visual que demuestra la actualización incremental de la app. A la izquierda la versión inicial (1.0.0) y a la derecha la versión actualizada (1.0.1) en el dispositivo físico o en el panel de versiones.", desc_style))

    box_left = make_placeholder_box("Antes: Versión 1.0.0<br/>(Pantalla inicial)", 240)
    box_right = make_placeholder_box("Después: Versión 1.0.1<br/>(Pantalla actualizada)", 240)
    compare_table = Table([[box_left, box_right]], colWidths=[255, 255])
    compare_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(compare_table)

    story.append(PageBreak())

    # ==================== SECCIÓN 6: BITÁCORA DE QA ====================
    story.append(Paragraph("6. Bitácora de QA (Máximo 1 página)", h1_style))
    story.append(Paragraph("Control de versiones, incidencias encontradas y estado de aprobación de las pruebas realizadas durante el ciclo de distribución.", desc_style))

    qa_headers = [
        Paragraph("<b>Versión</b>", meta_style),
        Paragraph("<b>Fecha</b>", meta_style),
        Paragraph("<b>Cambios Principales</b>", meta_style),
        Paragraph("<b>Incidencias Encontradas</b>", meta_style),
        Paragraph("<b>Estado</b>", meta_style),
    ]

    qa_row1 = [
        Paragraph("<b>1.0.0+1</b>", desc_style),
        Paragraph("01/11/2026", desc_style),
        Paragraph("Despliegue inicial de la app; interfaz base con identificación del estudiante y grupo QA; indicador visual 'Versión 1.0.0'; contador con botones de incrementar y reiniciar.", desc_style),
        Paragraph("<i>[PENDIENTE: Escribe incidencia o 'Ninguna']</i>", desc_style),
        Paragraph("<b>[PENDIENTE: Aprobado]</b>", desc_style),
    ]

    qa_row2 = [
        Paragraph("<b>1.0.1+2</b>", desc_style),
        Paragraph("01/11/2026", desc_style),
        Paragraph("Actualización incremental; nuevo indicador visual 'Versión 1.0.1'; cambio en esquema de colores a Teal/Verde; botón de decremento; verificación de actualización sobre paquete previo.", desc_style),
        Paragraph("<i>[PENDIENTE: Escribe incidencia o 'Ninguna']</i>", desc_style),
        Paragraph("<b>[PENDIENTE: Aprobado]</b>", desc_style),
    ]

    qa_table = Table([qa_headers, qa_row1, qa_row2], colWidths=[55, 65, 175, 145, 80])
    qa_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#DBEAFE')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1E3A8A')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#93C5FD')),
        ('PADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(qa_table)

    story.append(Spacer(1, 25))
    story.append(Paragraph("<b>Conclusiones del Proceso de Pruebas:</b>", h1_style))
    story.append(Paragraph("El ciclo de distribución mediante Firebase App Distribution permitió una entrega ágil a testers sin requerir publicación en tiendas comerciales (Google Play Store). El flujo GitFlow garantizó el orden en el control de versiones y el despliegue incremental (1.0.0 → 1.0.1) se ejecutó de forma transparente en el dispositivo de pruebas.", desc_style))

    story.append(Spacer(1, 30))
    story.append(Paragraph("<b>Firma del Responsable de Pruebas:</b> ___________________________<br/>Johan Eliu Salgado Castro", meta_style))

    doc.build(story)
    print("PDF generado exitosamente:", filename)

if __name__ == '__main__':
    out_pdf = os.path.join(os.path.dirname(__file__), "evidencias_taller1_app_distribution.pdf")
    create_evidence_pdf(out_pdf)
