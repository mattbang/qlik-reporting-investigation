[English](README.md) | **Deutsch**

# Management-Reporting mit Qlik skalieren

**Aus wiederkehrender regionaler Präsentationsvorbereitung einen wiederverwendbaren Reporting-Service entwickeln.**

Management-Präsentationen bezogen ihre Inhalte aus mehreren Qlik-Anwendungen. Dennoch mussten Länder und Funktionen ihre Präsentationen weiterhin einzeln zusammenstellen. Die Herausforderung lag im letzten Schritt: passende Varianten erzeugen und eine Verteilung auf Abruf oder nach Zeitplan praktikabel machen.

**Mein Beitrag:** Ich initiierte die Untersuchung, übersetzte die Bedürfnisse der Zielgruppen und die Vorgaben für Präsentationen in Anforderungen, arbeitete mich in die Reporting-Werkzeuge ein und baute Prototypen für Länder und Divisionen sowie für mehrere Anwendungen. Ich verglich die Optionen, bezog technische Fachpersonen ein und präsentierte Empfehlungen zu Vorlagen, Zugriff und Verantwortung.

**Ergebnis und Status:** funktionsfähige Berichtsbeispiele und eine Umsetzungsempfehlung. Eine breitere Einführung setzte eine zentrale Verantwortung und koordinierte Zugriffe voraus, die nicht geschaffen wurden. Der unten beschriebene öffentliche Generator ist eine neue Demonstration mit fiktiven Daten. Er erzeugt Dateien für ausgewählte Berichtsumfänge, ohne sich mit Qlik zu verbinden oder die Dateien zu versenden.

[Geschäftliche Fallstudie lesen](https://matthew-bangle-data-portfolio.mattbangle.chatgpt.site/de/work/reporting-automation-adoption) · [Öffentliche Demonstration ausführen](#demonstration-ausführen)

![Fiktive Länder- und Produktberichte, die aus einer gemeinsamen Vorlage zusammengestellt werden](assets/report-stack.png)

*Aktuelle Demonstration mit synthetischen Daten: gemeinsame Berichtsinhalte für unterschiedliche Zielgruppen. Zahlen des Arbeitgebers sind ausgeschlossen.*

## Was die Untersuchung zeigte

Wiederverwendbare Vorlagen konnten die wiederholte Vorbereitung von Präsentationen vereinfachen. Ein überzeugender Prototyp war jedoch nur ein Teil der Lösung. Der vorgeschlagene übergreifende Service benötigte auch koordinierte Anwendungszugriffe, eine klar benannte verantwortliche Person und geregelte Wartung. Diese betrieblichen Voraussetzungen wurden für eine breitere Einführung nicht geschaffen.

Mein Beitrag war technisch und organisatorisch: die Optionen so konkret machen, dass sie sich bewerten lassen, und anschliessend die für eine Einführung nötigen Entscheidungen benennen. Die Lehre daraus: das Betriebsmodell parallel zum Machbarkeitsnachweis entwickeln.

## Anforderungen hinter den Prototypen

Regionale Management-Präsentationen kombinierten Informationen aus mehreren Qlik-Anwendungen. Teams stellten wiederholt ähnliche Pakete aus Daten und Visualisierungen zusammen, die bereits an anderer Stelle gepflegt wurden. Ein wiederverwendbarer Ansatz musste vertraute Präsentationsstandards erhalten, mehrere Anwendungen verbinden und den passenden Länder- und Divisionsumfang auswählen.

| Geschäftliche Anforderung | Meine Arbeit | Unterstützte Entscheidung |
| --- | --- | --- |
| Wiederkehrende Länder- und Divisionsberichte | Vorlagen gebaut und Filter, Ebenen sowie Empfängerumfang untersucht | Wie eine Vorlage passende Varianten erzeugen kann |
| Informationen aus mehreren Anwendungen verbinden | Tabular Reporting, Application Automation und Subscriptions verglichen | Welcher Ansatz zur Reporting-Anforderung passt |
| Vertraute Standards für Management-Präsentationen erhalten | Layouts nachgebildet und Typografie, Raster und Platzierung verglichen | Was umsetzbar war und wo weitere Anpassungen nötig waren |
| Unklare Werkzeugfunktionen klären | Technische Fachpersonen anhand von Beispielen und konkreten Anforderungen konsultiert | Machbarkeit und verbleibende Abhängigkeiten |
| Einen dauerhaft betreibbaren Ansatz schaffen | Wiederverwendbare zentrale Vorlagen vorgeschlagen und Verantwortungsbedarf benannt | Was vor einer breiteren Einführung zu vereinbaren war |

Berater halfen, die Machbarkeit zu klären. Sie erstellten die hier gezeigten Prototypen nicht. Der Werkzeugvergleich beschreibt die Untersuchung von 2024 und ist keine aktuelle Kaufempfehlung.

## Einen zielgruppenspezifischen Bericht ansehen

Das aktuelle fiktive Beispiel erzeugt **12 unterschiedliche Folien, die in acht Berichtspaketen mit ausgewähltem Umfang zusammengestellt werden**, mit insgesamt 24 Folienplatzierungen. Die Diagramme vergleichen die Unternehmensentwicklung mit dem Wachstum des Gesamtmarkts, dem Marktanteil und durchschnittlichen Verkaufspreisen. Diese Zahlen beschreiben die öffentliche Demonstration und kein historisches Produktionsvolumen.

[Diagramme und Berechnungsdefinitionen](docs/reading-the-demo.md) · [Bearbeitbare PowerPoint-Datei](reports/Country-Product-Report.pptx) · [Studien zum Präsentationslayout](docs/layout-study.md)

## Demonstration ausführen

Python · HTML/SVG · PowerPoint · Untersuchung von Qlik-Reporting

Python 3.9 oder neuer; der HTML/SVG-Generator benötigt keine zusätzlichen Bibliotheken:

```sh
python3 demo/build.py
python3 -m unittest discover -s tests -v
```

Das Repository herunterladen und `reports/index.html` lokal öffnen. Der Generator erstellt zwölf Länder-/Produktgruppenfolien, sechs Länder-/Divisionspakete und zwei regionale Divisionspakete. Er schreibt Dateien und versendet keine E-Mails. Die Empfängeradressen sind fiktiv und verwenden `example.invalid`.

Das Beispiel demonstriert die Auswahl des Berichtsumfangs und die Berichtserzeugung. Es führt Qlik nicht aus, implementiert dessen Zugriffskontrollen nicht und bildet die ursprüngliche Automatisierung nicht nach. Die PowerPoint-Datei ist eine separate Präsentation derselben fiktiven Daten. Der Befehl erzeugt die HTML-, SVG-, CSV- und JSON-Ausgaben neu.

## Belege und weiterführende Dokumentation

- [Untersuchung und Entscheidungen](docs/case-study.md): was ich initiierte, erlernte, baute und empfahl.
- [Vergleich der Ansätze](docs/approach-comparison.md): Abwägungen anhand der geschäftlichen Anforderung.
- [Layoutstudie](docs/layout-study.md): erhaltene Iterationen und Grenzen bei der Ausrichtung.
- [Belege und Umfang](docs/evidence.md): zeitgenössische Unterlagen, rückblickende Darstellung und neue Demonstrationsmaterialien.

Die vertiefende technische Dokumentation ist auf Englisch.

Umfassendere Einsparungen bei der Vorbereitung blieben mögliche Vorteile. Die Automatisierung des wiederkehrenden Marktanteilsberichts an anderer Stelle meines Portfolios war ein separates Vorhaben. Die dort geschätzte monatliche Einsparung wird hier nicht erneut angerechnet.

Originalzahlen des Arbeitgebers, vollständige Präsentationen, Korrespondenz, Empfängerlisten, Tenant-Links und Konfiguration bleiben privat. Das öffentliche Material enthält begrenzte Layoutausschnitte ohne Finanzdaten und eine vollständig fiktive Demonstration.

[Matthew Bangle auf LinkedIn](https://www.linkedin.com/in/matthew-bangle/) · [Vollständiges Portfolio](https://matthew-bangle-data-portfolio.mattbangle.chatgpt.site/de/work)
