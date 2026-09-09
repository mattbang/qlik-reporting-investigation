# Reporting approaches I investigated

This comparison summarises my documented evaluation in 2024. It is historical project evidence, not a statement of current Qlik product specifications.

| Requirement | Tabular Reporting | Application Automation |
| --- | --- | --- |
| Structured reports with repeated country/product sections | A strong fit for Excel-based templates, levels and pages. I generated and distributed examples. | Could assemble a presentation workflow, but required more orchestration and presentation-sheet preparation. |
| Sources across multiple existing apps | My investigation identified a single-app constraint for an individual report. Combining the full management package that way would have required consolidating sources and duplicating maintained objects. | The multi-app capability was central to my recommendation: reuse existing sheets across applications. |
| Output format | Excel and PDF were the formats evaluated. It did not meet the PowerPoint requirement in my tests and documented comparison. | Evaluated for PowerPoint management packages built from presentation-oriented sheets. |
| Country/division variants and distribution | Template filters, levels and recipient lists supported scoped output. Filter behaviour and the distinction between country and regional variants required testing. | Recipient handling and existing access rules formed part of the requirement and consultant discussion. Correct permission setup remained an implementation dependency. |
| Visual fidelity | Flexible Excel template layout, with reported constraints around chart colours, object support and export/page formatting. | Sheet layouts could closely reproduce the presentation style, but grid granularity, fonts and alignment required refinement. |
| Maintenance | Convenient within a suitable app; duplicating cross-app reporting content would introduce additional maintenance. | Potential to reuse governed sources and shared templates, but needed coordinated app access and central ownership. |
| Learning and setup | Initial add-in setup, permissions and filtering behaviour needed investigation. | More complex orchestration, presentation-template design and mail-connector setup. |
| Best role in my recommendation | Detailed, repeated tabular and country/product reporting. | A broader management package drawing on several maintained applications. |

## PowerPoint Subscriptions: the third option

I also evaluated subscriptions, and revisited them as functionality became available in the working environment. An October message records the appeal of a simpler way to schedule PowerPoint emails. A retained November system email explicitly describes a subscription and includes a PowerPoint attachment.

Subscriptions were useful for distributing a defined application view. They did not, by themselves, remove the need to establish ownership and access for the wider multi-application reporting service I proposed.

## Important distinctions

- A recipient list is not a substitute for source-data authorisation.
- A visually correct export is not proof that every recipient received the correct data scope.
- The consultant discussion supported feasibility with constraints; it did not establish that a global rollout had happened.
- The potential reduction in regional preparation effort is a business rationale. This project does not claim measured global savings.
