# Reusable Management Reporting: From Prototype to Recommendation

**Tested how existing Qlik content could become reusable management presentations—and identified what wider adoption would require.**

I initiated the investigation, learned the reporting tools, built prototypes and compared approaches against country, division and presentation requirements. The deliverable was a practical recommendation supported by working examples and a clearer view of ownership and access dependencies.

[Open sample slides](reports/Country-Product-Report.pptx) · [Investigation and decisions](docs/case-study.md) · [Website case study](https://matthew-bangle-data-portfolio.mattbangle.chatgpt.site/work/reporting-automation-adoption)

![Fictional country and product report variants assembled from a shared template](assets/report-stack.png)

*Current synthetic demonstration: shared report content assembled for different audiences. Employer figures are excluded.*

## What the investigation established

Reusable templates could address repeated presentation preparation, but a convincing prototype was only part of the solution. The proposed broader service also needed coordinated application access, a named owner and maintenance responsibilities. Those operating conditions were not established for a wider rollout.

My contribution was both technical and organisational: make the options concrete enough to evaluate, then identify the decisions needed for adoption. The lesson I would apply again is to develop the operating model alongside the proof of concept.

## Requirements behind the prototypes

Regional management presentations combined information from several Qlik applications. Teams repeatedly rebuilt similar packages from data and visualisations already maintained elsewhere. A reusable approach needed to preserve familiar presentation standards, combine applications and select the right country and division scope.

| Business requirement | Work I carried out | Decision it informed |
| --- | --- | --- |
| Repeat country and division reports | Built templates and explored filters, levels and recipient scope | How one template could produce relevant variants |
| Combine information across applications | Compared Tabular Reporting, Application Automation and Subscriptions | Which approach fitted the reporting requirement |
| Preserve familiar management presentation standards | Recreated layouts and compared typography, grids and placement | What was achievable and what needed refinement |
| Resolve uncertain tool capabilities | Consulted technical specialists with examples and explicit requirements | Feasibility and remaining dependencies |
| Make the approach sustainable | Proposed reusable central templates and identified ownership needs | What had to be agreed before a wider rollout |

Consultants helped clarify feasibility; they did not build the prototype work presented here. The tool comparison describes the 2024 investigation, not a current product-buying recommendation.

## Inspect an audience-specific report

The current fictional example creates **12 unique slides assembled into eight scoped packages**, with 24 slide placements. The charts compare company performance with total-market growth, market share and average selling prices. These counts describe the public demonstration, not historical production volume.

[Read the charts and calculation definitions](docs/reading-the-demo.md) · [Editable PowerPoint](reports/Country-Product-Report.pptx) · [Presentation-layout studies](docs/layout-study.md)

## Run the demonstration

Python · HTML/SVG · PowerPoint · Qlik reporting investigation

Python 3.9 or later; no third-party dependencies for the HTML/SVG generator:

```sh
python3 demo/build.py
python3 -m unittest discover -s tests -v
```

Download the repository and open `reports/index.html` locally. The generator creates twelve country/product-group slides, six country/division packages and two regional/division packages. It writes files and sends no email. Recipient addresses are fictional and use `example.invalid`.

The example demonstrates scope selection and report generation. It does not run Qlik, implement its access controls or reproduce the original automation. The PowerPoint is a separate presentation of the same fictional data; the command rebuilds HTML, SVG, CSV and JSON outputs.

## Evidence and further reading

- [Investigation and decisions](docs/case-study.md): what I initiated, learned, built and recommended.
- [Approach comparison](docs/approach-comparison.md): trade-offs against the business requirement.
- [Layout study](docs/layout-study.md): retained iterations and alignment limitations.
- [Evidence and scope](docs/evidence.md): contemporary records, retrospective account and new demonstration material.

Wider preparation savings remained potential benefits. The recurring market-share report automation elsewhere in my portfolio was separate work; its estimated monthly saving is not assigned again here.

Original employer figures, full presentations, correspondence, recipient lists, tenant links and configuration stay private. Public material includes limited non-financial layout excerpts and a fully fictional demonstration.

[Matthew Bangle on LinkedIn](https://www.linkedin.com/in/matthew-bangle/) · [Full portfolio](https://matthew-bangle-data-portfolio.mattbangle.chatgpt.site/work)
