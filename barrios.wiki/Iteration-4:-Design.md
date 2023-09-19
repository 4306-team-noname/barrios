The results of the system design process are recorded in the **System Design Document** (SDD). This document completely describes the system at the architecture level, including subsystems and their services, hardware mapping, data management, access control, global software control structure, and boundary conditions. The SDD should define a virtual machine that implements all requirements in the RAD, and it should provide a foundational guide for further implementation details all the way to an executable solution.

Note that the SDD is a "live" document that should be incrementally expanded and refined during review cycles.

**Audience**

The audience for the SDD includes the software architect and lead members (liaisons) from each subsystem development team.

## To do:
1. Complete Software Design Ddocument (SDD) (below) and submit a PDF copy to **Blackboard**,
2. Continue implementation,
   1. Actively use GitHub for (a) source code development, (b) project management, (c) issue resolution. These will be graded according to individual team members' activity and participation.
   2. Update wiki pages for requirement and design changes during development.
   3. Make sure that your design and implementation are synced.

## System Design Document (SDD)
1. **Introduction**
   1. Purpose of the system
   2. Design goals
   3. Definitions, acronyms, and abbreviations
   4. References
   5. Overview
2. **Current software architecture**<br/>
   _Explain the existing system (if you do not have, skip)._
3. **Proposed software architecture**
   1. Overview
   2. Subsystem decomposition<br/>
      _A [UML Package Diagram](https://www.uml-diagrams.org/package-diagrams-overview.html) to depict the packages or subsystems in your system._
   3. Hardware/software mapping<br/>
      _A [UML Deployment Diagram](https://www.conceptdraw.com/examples/online-shopping-hardware-software-mapping) to depict what software components are deployed on what kind of hardware components._
   4. Persistent data management<br/>
      _A database model such as [Entity-Relationship Diagram](https://drawio-app.com/entity-relationship-diagrams-with-draw-io/) ([video](https://www.youtube.com/watch?v=lAtCySGDD48)) or a [NoSQL data model](https://docs.mongodb.com/manual/core/data-modeling-introduction/)._
   5. Access control and security<br/>
      _Access matrix, which users access which parts of the software._
   6. Global software control<br/>
      _Describe how the global software control is implemented. In particular, this section should describe how requests are initiated and how subsystems synchronize. This section should list and address synchronization and concurrency issues._
   7. Boundary conditions<br/>
      _List and describe the boundary conditions: startup, shutdown, and error behavior of the system._
4. **Subsystem services**<br/>
      _UML Class Diagram for each subsystem in 3.ii_
- Glossary

Appendix. Project Plan
- Project tasks (product backlog) and time needed to implement with a deadline.

_Reference._
- [SDD explanations](https://www.cs.fsu.edu/~lacher/courses/COP3331/sdd.html).