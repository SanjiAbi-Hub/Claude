# -*- coding: utf-8 -*-
"""Erzeugt eine ausgefuellte Version des Arbeitsblatts AB3 'Hauptsache weit'."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether)

# ---- Farben fuer die drei Kategorien (Aufgabe 4) -------------------------
BLAU   = "#1d4ed8"   # Aeusseres
GRUEN  = "#15803d"   # Charakter
ORANGE = "#c2410c"   # Soziales Umfeld

def mark(text, color):
    return f'<u><font color="{color}"><b>{text}</b></font></u>'

# ---- Originaltext, Zeile fuer Zeile --------------------------------------
# (Zeilennummern wie im Arbeitsblatt, Markierung nur in Zeile jeweils einmal)
lines = [
 "Und weg, hatte er gedacht. " + mark("Die Schule war zu Ende", ORANGE) + ", das Leben noch nicht, hatte noch nicht",
 "begonnen, das Leben. " + mark("Er hatte nicht viel Angst davor, weil er noch keine Enttäuschungen", GRUEN),
 mark("kannte", GRUEN) + ". Er war " + mark("ein schöner Junge", BLAU) + " " + mark("mit langen dunklen Haaren", BLAU) + ", " + mark("er spielte Gitarre, komponierte", GRUEN),
 mark("am Computer", GRUEN) + " und dachte, " + mark("irgendwie werde ich wohl später nach London gehen, was Kreatives", GRUEN),
 mark("machen", GRUEN) + ". Aber das war später.",
 "Und nun?",
 "Warum kommt der Spaß nicht? Der Junge hockt in einem Zimmer, das Zimmer ist grün, wegen",
 "der Neonleuchte, es hat kein Fenster und der Ventilator ist sehr laut. Schatten huschen über",
 "den Betonboden, das Glück ist das nicht, eine Wolldecke auf dem Bett, auf der schon einige",
 "Kriege ausgetragen wurden. Magen gegen Tom Yan, Darm gegen Curry. Immer verloren, die",
 "Eingeweide. " + mark("Der Junge ist 18", BLAU) + ", und jetzt aber Asien hatte er sich gedacht. " + mark("Mit 1000 Dollar", ORANGE) + " durch",
 "Thailand, Indien, Kambodscha, drei Monate unterwegs und dann wieder heim, nach",
 mark("Deutschland", ORANGE) + ". Das ist so eng, so langweilig, jetzt was erleben und vielleicht nie zurück. Hast du",
 "keine Angst, hatten " + mark("die blassen Freunde zu Hause", ORANGE) + " gefragt, so ganz alleine? Nein, hatte er",
 "geantwortet, man lernt ja so viele Leute kennen unterwegs. Bis jetzt hatte er hauptsächlich",
 mark("Mädchen kennen gelernt", ORANGE) + ", nett waren die schon, wenn man Leute mag, die einen bei jedem",
 "Satz anfassen. Mädchen, die aussahen wie dreißig und doch so alt waren wie er, seit Monaten",
 "unterwegs, die Mädchen, da werden sie komisch. Übermorgen würde er in Laos sein, da mag",
 "er jetzt gar nicht daran denken, in seinem hässlichen Pensionszimmer, " + mark("muss Obacht geben,", GRUEN),
 mark("dass er sich nicht aufs Bett wirft und weint", GRUEN) + ", auf die Decke, wo schon die anderen Dinge drauf",
 "sind. In dem kleinen Fernseher kommen nur Leute vor, die ihm völlig fremd sind, das ist das",
 "Zeichen, dass man einsam ist, wenn man die Fernsehstars eines Landes nicht kennt und die",
 "eigenen keine Bedeutung haben. " + mark("Der Junge sehnt sich nach Stefan Raab, nach Harald Schmidt", GRUEN),
 "und Echt1. Er merkt weiter, dass er gar nicht existiert, wenn es nichts hat, was er kennt. Wenn",
 "er keine Zeitung in seiner Sprache kaufen kann, keine Klatschgeschichten über einheimische",
 "Prominente lesen, wenn keiner anruft und fragt, wie es ihm geht. Dann gibt es ihn nicht. Denkt",
 "er. Und ist unterdessen aus seinem heißen Zimmer in die heiße Nacht gegangen, hat fremdes",
 "Essen vor sich, von einer fremdsprachigen Serviererin gebracht, die sich nicht für ihn",
 "interessiert, wie niemand hier. Das ist wie tot sein, denkt der Junge. Weit weg von zu Hause,",
 "um anderen beim Leben zusehen, könnte man umfallen und sterben in der tropischen Nacht",
 "und niemand würde weinen darum. " + mark("Jetzt weint er doch", GRUEN) + ", denkt an die lange Zeit, die er noch",
 "rumbekommen muss, alleine in heißen Ländern mit seinem Rucksack, und das stimmt so gar",
 "nicht mit den Bildern überein, die er zu Hause von sich hatte. Wie er entspannt mit",
 "Wasserbüffeln spielen wollte, in Straßencafés sitzen und " + mark("cool sein", GRUEN) + ". Was ist, ist einer mit",
 mark("Sonnenbrand", BLAU) + " und " + mark("Heimweh", GRUEN) + " nach den Stars zu Hause, die sind wie ein Geländer zum Festhalten.",
 "Er geht durch die Nacht, selbst die Tiere reden ausländisch, und dann sieht er etwas, sein Herz",
 "schlägt schneller. Ein Computer, ein Internet-Café. Und er setzt sich, schaltet den Computer",
 "an, liest seine E-Mails. Kleine Sätze von seinen Freunden, und denen antwortet er, dass es ihm",
 "gut gehe und alles großartig ist, und er schreibt und schreibt und es ist auf einmal völlig egal,",
 "dass zu seinen Füßen ausländische Insekten so groß wie Meerkatzen herumlaufen, dass das",
 "fremde Essen im Magen drückt. Er schreibt " + mark("seinen Freunden", ORANGE) + " über die kleinen Katastrophen",
 "und die fremde Welt um ihn verschwimmt, er ist nicht mehr allein, taucht in den Bildschirm",
 "ein, der ist wie ein weiches Bett, er denkt an Bill Gates und Fred Apple 2, er schickt ein Mail an",
 "Sat 1, und für ein paar Stunden ist er wieder am Leben, in der heißen Nacht weit weg von zu",
 "Hause.",
]

# ---- Styles --------------------------------------------------------------
styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Title'], fontSize=15, spaceAfter=2, textColor=colors.HexColor('#0f172a'))
SUB = ParagraphStyle('SUB', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#475569'), spaceAfter=8)
TXT = ParagraphStyle('TXT', parent=styles['Normal'], fontName='Helvetica', fontSize=8.6, leading=11.2)
LN  = ParagraphStyle('LN', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, textColor=colors.HexColor('#94a3b8'), alignment=2)
TASK= ParagraphStyle('TASK', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, textColor=colors.HexColor('#0f172a'), spaceBefore=12, spaceAfter=5)
ANS = ParagraphStyle('ANS', parent=styles['Normal'], fontSize=9.6, leading=13.4, spaceAfter=4)
QUO = ParagraphStyle('QUO', parent=styles['Normal'], fontSize=9.2, leading=12.5, textColor=colors.HexColor('#334155'))
CELL= ParagraphStyle('CELL', parent=styles['Normal'], fontSize=9.2, leading=13)
LEG = ParagraphStyle('LEG', parent=styles['Normal'], fontSize=9, leading=12)
HEAD= ParagraphStyle('HEAD', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.6, textColor=colors.white, alignment=1)

story = []
story.append(Paragraph("Sibylle Berg: <i>Hauptsache weit</i> (2001) &ndash; ausgefülltes Arbeitsblatt", H1))
story.append(Paragraph("Deutsch &bull; Inhaltsangaben verfassen &bull; Markierungen zu Aufgabe 4", SUB))
story.append(HRFlowable(width='100%', thickness=1, color=colors.HexColor('#cbd5e1'), spaceAfter=8))

# Legende
leg = Table([[
    Paragraph(mark("Äußeres", BLAU), LEG),
    Paragraph(mark("Charakter", GRUEN), LEG),
    Paragraph(mark("Soziales Umfeld", ORANGE), LEG),
]], colWidths=[5.5*cm, 5.5*cm, 5.5*cm])
leg.setStyle(TableStyle([('BOTTOMPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),2)]))
story.append(leg)

# Text als Tabelle (Zeilennr. + Text)
rows = []
for i, ln in enumerate(lines, start=1):
    num = str(i) if (i == 1 or i % 5 == 0) else ""
    rows.append([Paragraph(num, LN), Paragraph(ln, TXT)])
txt_table = Table(rows, colWidths=[0.8*cm, 16.0*cm])
txt_table.setStyle(TableStyle([
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('TOPPADDING',(0,0),(-1,-1),0.6),
    ('BOTTOMPADDING',(0,0),(-1,-1),0.6),
    ('LEFTPADDING',(0,0),(-1,-1),2),
    ('RIGHTPADDING',(0,0),(-1,-1),2),
    ('LINEBEFORE',(1,0),(1,-1),0.5,colors.HexColor('#e2e8f0')),
]))
story.append(txt_table)
story.append(Paragraph("<font size=7 color='#94a3b8'>1 Deutsche Popgruppe, die sich 2002 auflöste &nbsp;&nbsp; 2 Anspielung auf Fred C. Anderson, 1996&ndash;2004 CFO von Apple Computer Inc.</font>", SUB))

# ---- Aufgabe 1 -----------------------------------------------------------
story.append(Paragraph("1) Erkläre mit eigenen Worten, was jeweils gemeint ist.", TASK))

def cell(t, style=CELL): return Paragraph(t, style)
a1 = [
 [Paragraph("Textstelle", HEAD), Paragraph("Erklärung", HEAD)],
 [cell('&bdquo;Er merkt weiter, dass er gar nicht existiert, wenn er nichts hat, was er kennt.&ldquo; (Z.&nbsp;25&nbsp;f.)', QUO),
  cell('Der Junge fühlt sich in der fremden Umgebung wie nicht vorhanden. Er definiert sich über Vertrautes &ndash; bekannte Menschen, Medien, seine Sprache. Fehlt ihm all das, verliert er das Gefühl für die eigene Identität und meint, es gäbe ihn selbst gar nicht mehr.')],
 [cell('&bdquo;(&hellip;) Er schreibt und schreibt und es ist auf einmal völlig egal, dass zu seinen Füßen ausländische Insekten so groß wie Meerkatzen herumlaufen&hellip;&ldquo; (Z.&nbsp;43&nbsp;ff.)', QUO),
  cell('Sobald er am Computer mit seinen Freunden schreibt, blendet er die unangenehme, fremde Umwelt völlig aus. Die Ablenkung ist so stark, dass ihn sogar die ekligen, riesigen Insekten nicht mehr stören &ndash; die Verbindung nach Hause ist ihm wichtiger als die Wirklichkeit um ihn herum.')],
 [cell('&bdquo;Er schreibt seinen Freunden (&hellip;), er ist nicht mehr allein.&ldquo; (Z.&nbsp;44&nbsp;ff.)', QUO),
  cell('Durch den Kontakt über das Internet fühlt er sich mit seinen Freunden verbunden, obwohl er körperlich tausende Kilometer entfernt und tatsächlich ganz allein ist. Die digitale Kommunikation nimmt ihm für einen Moment das Gefühl der Einsamkeit.')],
 [cell('&bdquo;(&hellip;) Bildschirm (&hellip;), der ist wie ein weiches Bett.&ldquo; (Z.&nbsp;46&nbsp;f.)', QUO),
  cell('Der Vergleich zeigt, dass der Bildschirm für ihn Geborgenheit, Schutz und Trost bedeutet. Wie ein weiches Bett gibt ihm die Online-Welt Sicherheit und ein Zuhause-Gefühl mitten in der fremden, bedrohlichen Umgebung.')],
]
t1 = Table(a1, colWidths=[6.3*cm, 10.5*cm])
t1.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#334155')),
    ('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#cbd5e1')),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, colors.HexColor('#f8fafc')]),
    ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
    ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
]))
story.append(t1)

# ---- Aufgabe 2 -----------------------------------------------------------
story.append(Paragraph("2) Welche Rolle spielen Medien im Leben des Jungen?", TASK))
story.append(Paragraph("Medien sind für den Jungen ein <b>Anker und Rückzugsort</b>. Fernsehen und deutsche Stars (Stefan Raab, Harald Schmidt, Echt) und vor allem das Internet geben ihm Halt und ein Stück Heimat. Über E-Mails hält er Kontakt zu seinen Freunden und fühlt sich dadurch wieder lebendig und weniger einsam.", ANS))
story.append(Paragraph("Gleichzeitig zeigt die Geschichte das <b>kritisch</b>: Statt sich auf das fremde Land einzulassen, <b>flüchtet</b> er in die vertraute Medienwelt. Die Medien ersetzen ihm reale Begegnungen und werden zu einer Art Lebensersatz &ndash; erst am Bildschirm ist er &bdquo;für ein paar Stunden &hellip; wieder am Leben&ldquo;. So überbrücken die Medien seine Einsamkeit, verhindern aber zugleich echte Erfahrungen auf der Reise.", ANS))

# ---- Aufgabe 3 -----------------------------------------------------------
story.append(Paragraph("3) Würdest du zu einer solchen Reise raten oder abraten? Mit welchen Argumenten?", TASK))
story.append(Paragraph("<b>Meine Position:</b> Ich würde grundsätzlich dazu <b>raten</b> &ndash; aber nur mit guter Vorbereitung.", ANS))
story.append(Paragraph("<b>Dafür spricht:</b> Eine solche Reise erweitert den Horizont, macht selbstständig und selbstbewusst. Man lernt fremde Kulturen und viele neue Menschen kennen und sammelt Erfahrungen, die man ein Leben lang nicht vergisst.", ANS))
story.append(Paragraph("<b>Dagegen spricht (wie in der Geschichte):</b> Allein unterwegs können Einsamkeit, Heimweh und ein Kulturschock stark belasten. Wer sich innerlich nicht auf das Fremde einlässt, fühlt sich schnell verloren &ndash; so wie der Junge, der vor der Reise in die Medien flüchtet.", ANS))
story.append(Paragraph("<b>Mein Rat:</b> Fahr los, aber bereite dich vor (Sprache, Land, Route), reise anfangs vielleicht nicht völlig allein und lass dich wirklich auf das Land ein, statt dich nur hinter dem Handy oder Laptop zu verstecken. Dann überwiegen die Chancen klar die Risiken.", ANS))

# ---- Aufgabe 4 -----------------------------------------------------------
a4_head = Paragraph("4) Was erfahren wir über die Hauptfigur? (Markierungen im Text oben &ndash; hier zugeordnet)", TASK)

def bullets(items):
    return Paragraph("<br/>".join("&bull; " + it for it in items), CELL)

a4 = [
 [Paragraph("Äußeres", HEAD), Paragraph("Charakter", HEAD), Paragraph("Soziales Umfeld", HEAD)],
 [bullets([
    "schöner Junge (Z.&nbsp;3)",
    "lange, dunkle Haare (Z.&nbsp;3)",
    "18 Jahre alt (Z.&nbsp;11)",
    "Sonnenbrand (Z.&nbsp;35)",
  ]),
  bullets([
    "unerfahren / naiv &ndash; kennt noch keine Enttäuschungen, hat kaum Angst (Z.&nbsp;2&nbsp;f.)",
    "kreativ &amp; musikalisch &ndash; spielt Gitarre, komponiert am Computer (Z.&nbsp;3&nbsp;f.)",
    "träumerisch / unentschlossen &ndash; will &bdquo;irgendwie&ldquo; nach London, &bdquo;was Kreatives machen&ldquo; (Z.&nbsp;4&nbsp;f.)",
    "sensibel / den Tränen nah &ndash; muss aufpassen, nicht zu weinen; &bdquo;jetzt weint er doch&ldquo; (Z.&nbsp;19&nbsp;f., 31)",
    "heimwehkrank / anhänglich &ndash; sehnt sich nach den Stars von zu Hause, Heimweh (Z.&nbsp;23, 35)",
    "will &bdquo;cool&ldquo; wirken, ist es aber nicht (Z.&nbsp;34)",
  ]),
  bullets([
    "Schulabgänger &ndash; gerade mit der Schule fertig (Z.&nbsp;1)",
    "kommt aus Deutschland (Z.&nbsp;12&nbsp;f.)",
    "hat Freunde zu Hause (&bdquo;die blassen Freunde&ldquo;) (Z.&nbsp;14)",
    "lernt unterwegs vor allem Mädchen kennen (Z.&nbsp;15&nbsp;f.)",
    "reist mit kleinem Budget (1000 Dollar) (Z.&nbsp;11)",
    "hält per E-Mail Kontakt zu den Freunden (Z.&nbsp;40)",
  ]),
 ],
]
t4 = Table(a4, colWidths=[5.0*cm, 6.8*cm, 5.0*cm])
t4.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(0,0),colors.HexColor(BLAU)),
    ('BACKGROUND',(1,0),(1,0),colors.HexColor(GRUEN)),
    ('BACKGROUND',(2,0),(2,0),colors.HexColor(ORANGE)),
    ('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#cbd5e1')),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
    ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
]))
story.append(KeepTogether([a4_head, t4]))

doc = SimpleDocTemplate("/home/user/Claude/AB3_Sybille_Berg_ausgefuellt.pdf",
                        pagesize=A4, topMargin=1.3*cm, bottomMargin=1.3*cm,
                        leftMargin=1.6*cm, rightMargin=1.6*cm,
                        title="AB3 Hauptsache weit - ausgefuellt")
doc.build(story)
print("fertig")
