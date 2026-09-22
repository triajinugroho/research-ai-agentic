# Knowledge Unit CS2023 per Bahan Kajian (Referensi)

**Sumber:** `Revisi_2026_Kurikulum_OBE_IF_2025_2.xlsx` — sheet `6a. BK-KA-Knowledge Unit CS2023`  
**Status:** Final (disepakati s.d. sheet *Copy of (Ref) 15. Pemetaan MK-CPMK-SubCPMK*)  
**Kurikulum:** Kurikulum Informatika 2025 — Revisi 2026  
**Ekstraksi:** September 2026  

---

Tabel rujukan **166 Knowledge Unit** ACM/IEEE CS2023 yang menjadi rincian isi tiap
Bahan Kajian. Dipakai sebagai kamus istilah saat menyusun materi/Sub-CPMK, bukan sebagai
daftar wajib ajar.

> **Catatan:** sheet sumber berstatus *hidden* di berkas Excel dan kolom pemetaan ke mata kuliah
> UAI masih kosong (*Belum Dipetakan*). Gunakan sebagai referensi, bukan sebagai keputusan kurikulum.


## BK01 — Artificial Intelligence (`AI`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| AI-Introduction | Fundamental Issues | Konsep dan ruang lingkup AI, intelligent behavior, rasionalitas, representasi, problem solving, serta kapan pendekatan AI tepat digunakan. |
| AI-Search | Search | Pencarian state-space dan graph, uninformed/heuristic search, optimisasi, local search, adversarial/game search, serta trade-off kualitas-kinerja. |
| AI-KRR | Fundamental Knowledge Representation and Reasoning | Representasi pengetahuan dasar dan mekanisme reasoning untuk memodelkan fakta, relasi, aturan, ketidakpastian, dan keputusan. |
| AI-ML | Machine Learning | Supervised, unsupervised, reinforcement learning, generalization, evaluation, deep learning/generative methods, fairness, explainability, dan aplikasi. |
| AI-SEP | Applications and Societal Impact | Aplikasi AI dan dampak sosialnya: fairness, accountability, transparency, trust, bias, privacy, safety, misuse, dan tanggung jawab profesional. |
| AI-LRR | Logical Representation and Reasoning | Representasi logis dan penalaran berbasis propositional/first-order logic, inference, rules, constraint, dan reasoning simbolik. |
| AI-Probability | Probabilistic Representation and Reasoning | Model probabilistik, Bayes, conditional independence, probabilistic inference, graphical models, dan keputusan di bawah ketidakpastian. |
| AI-Planning | Planning | Formulasi goal/action/state, classical planning, planning under uncertainty, scheduling/decision sequences, dan evaluasi rencana. |
| AI-Agents | Agents and Cognitive Systems | Arsitektur agen, rational agents, autonomous behavior, multi-agent/cognitive systems, perception-action loop, dan koordinasi. |
| AI-NLP | Natural Language Processing | Representasi dan pemrosesan bahasa alami, language models, text analysis, generation, semantics, evaluation, dan aplikasi NLP. |
| AI-Robotics | Robotics | Persepsi, localization, mapping, motion/path planning, kinematics, control, autonomy, serta integrasi sensor-actuator. |
| AI-Vision | Perception and Computer Vision | Akuisisi dan representasi citra, segmentation, recognition, motion, generative vision, pattern recognition, dan multimodal perception. |

## BK02 — Algorithmic Foundations (`AL`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| AL-Foundational | Foundational Data Structures and Algorithms | Struktur data fundamental, ADT, arrays, records, linked structures, stacks/queues, trees, graphs, searching, sorting, hashing, dan operasi dasar. |
| AL-Strategies | Algorithmic Strategies | Paradigma brute force, decrease/divide-and-conquer, greedy, transform-and-conquer, dynamic programming, backtracking, branch-and-bound, heuristics, dan randomization. |
| AL-Complexity | Complexity | Analisis asymptotic, time/space complexity, recurrence, tractability/intractability, P/NP, NP-completeness, reductions, dan empirical performance. |
| AL-Models | Computational Models and Formal Languages | Finite automata, grammars/languages, pushdown automata, Turing machines, computability, decidability, dan batas fundamental komputasi. |
| AL-SEP | Society, Ethics, and the Profession | Dampak sosial/etika algoritma: efficiency vs resources, bias, accountability, sustainability, accessibility, dan konsekuensi pilihan algoritmik. |

## BK03 — Architecture and Organization (`AR`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| AR-Logic | Digital Logic and Digital Systems | Logika digital, combinational/sequential circuits, Boolean logic, representation hardware, FPGA, dan hubungan logika digital dengan sistem. |
| AR-Representation | Machine-Level Data Representation | Representasi bilangan, data, instruksi, encoding, floating point, endianness, dan keterbatasan representasi tingkat mesin. |
| AR-Assembly | Assembly Level Machine Organization | Instruction set, assembly, registers, addressing, control flow, calling conventions, interrupts, dan hubungan machine code dengan software. |
| AR-Memory | Memory Hierarchy | Registers-cache-main memory-storage, locality, cache design, virtual memory links, latency/bandwidth, coherence, dan performance trade-offs. |
| AR-IO | Interfacing and Communication | I/O, buses, interrupts, buffering, programmed/interrupt-driven I/O, DMA, external storage, sensors/actuators, dan device interfaces. |
| AR-Organization | Functional Organization | Datapath/control, pipelining, processor organization, instruction execution, multicore basics, dan struktur fungsional komputer. |
| AR-Performance-Energy | Performance and Energy Efficiency | Pengukuran/optimasi performance, latency/throughput, parallelism, energy/power, trade-off architecture, dan sustainability. |
| AR-Heterogeneity | Heterogeneous Architectures | CPU, GPU, accelerator, domain-specific hardware, heterogeneous memory/compute, programming implications, dan workload mapping. |
| AR-Security | Secure Processor Architectures | Hardware roots of trust, isolation, secure execution, side-channel/speculation issues, memory protection, dan dukungan hardware untuk security. |
| AR-Quantum | Quantum Architectures | Qubits, gates, measurement, quantum circuits, QPU architecture, control, error/noise considerations, dan pengantar algoritma/aplikasi quantum. |
| AR-SEP | Sustainability Issues | Dampak energi, material, lifecycle, e-waste, resource use, dan tanggung jawab keberlanjutan pada desain serta penggunaan arsitektur komputer. |

## BK04 — Data Management (`DM`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| DM-Data | The Role of Data and the Data Life Cycle | Peran data dan tahapan creation-processing-review/reporting-retention/retrieval-destruction serta governance sepanjang data lifecycle. |
| DM-Core | Core Database System Concepts | Tujuan/arsitektur DBMS, data independence, transactions, normalization overview, CRUD, declarative query, distributed/cloud basics, dan structured/unstructured data. |
| DM-Modeling | Data Modeling | Model konseptual dan logis, relational model, ER/UML, semi-structured/document/key-value representations, serta pemetaan kebutuhan ke model data. |
| DM-Relational | Relational Databases | Relational design, keys/integrity, schema mapping, functional dependency, normalization/denormalization, dan physical design. |
| DM-Querying | Query Construction | Relational algebra/SQL, selection-projection-join, aggregation, subqueries, update, constraints, query formulation, dan pemanfaatan declarative languages. |
| DM-Processing | Query Processing | Parsing/planning, access paths, join algorithms, indexing, optimization, cost estimation, external sorting, dan eksekusi query. |
| DM-Internals | DBMS Internals | Storage/buffer management, transactions, concurrency control, recovery, logging, indexing, system catalogs, dan implementasi internal DBMS. |
| DM-NoSQL | NoSQL Systems | Key-value, document, column, graph databases, consistency models, schema flexibility, scaling, use cases, dan trade-off terhadap relational systems. |
| DM-Security | Data Security and Privacy | Data privacy/security, PII, injection, access control, encryption at rest/in transit/in use, auditing, inferencing, laws/regulations, dan ethical handling. |
| DM-Analytics | Data Analytics | Exploratory analysis, data mining/ML links, acquisition/governance, fairness/bias, visualization, entity resolution, dan analytics lifecycle. |
| DM-Distributed | Distributed Databases/Cloud Computing | Distributed/parallel DBMS, replication, consistency, distributed transactions/query processing, client-server/cloud architectures, speedup dan scale-up. |
| DM-Unstructured | Semi-structured and Unstructured Databases | JSON/semi-structured storage, vectorized text/audio/video, indexing, compression, vector stores, query processing OLTP/OLAP, dan modern unstructured data systems. |
| DM-SEP | Society, Ethics, and the Profession | Privacy, ownership/custodianship, provenance/lineage, unintended uses, reliability, data security, scale, governance, dan konsekuensi sosial basis data. |

## BK05 — Foundations of Programming Languages (`FPL`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| FPL-OOP | Object-Oriented Programming | Object, class, state/behavior, inheritance, overriding, dynamic dispatch, exception handling, interfaces, polymorphism, dan OO design principles. |
| FPL-Functional | Functional Programming | Pure functions, immutability, recursion, higher-order functions, closures, algebraic data types, lazy/eager evaluation, dan functional composition. |
| FPL-Logic | Logic Programming | Facts, rules, unification, inference, declarative problem solving, backtracking, constraint logic, dan hubungan logic programming dengan formal reasoning. |
| FPL-Scripting | Shell Scripting | Automation scripts, piping, commands, environment variables, files, regex, processes, workflow, error handling, dan interaction dengan OS. |
| FPL-Event-Driven | Event-Driven and Reactive Programming | Events, callbacks/handlers, event loops, reactive streams, asynchronous control, GUI/network events, responsiveness, dan state management. |
| FPL-Parallel | Parallel and Distributed Computing | Language constructs untuk concurrency/parallel/distributed execution: threads/tasks, synchronization, message passing, futures, data parallelism, dan safety. |
| FPL-Aspect | Aspect-Oriented Programming | Cross-cutting concerns, aspects, join points, advice, weaving, modularization concern, serta trade-off maintainability dan complexity. |
| FPL-Types | Type Systems | Static/dynamic typing, type safety, inference, polymorphism, subtyping, generics, algebraic types, soundness, dan role of types in correctness/security. |
| FPL-Systems | Systems Execution and Memory Model | Runtime model, stack/heap, allocation, pointers/references, memory safety, calling/runtime conventions, concurrency memory model, dan systems-level execution. |
| FPL-Translation | Language Translation and Execution | Compilation, interpretation, virtual machines, intermediate representations, linking/loading, JIT, runtime systems, dan execution pipelines. |
| FPL-Abstraction | Program Abstraction and Representation | Abstract syntax/representations, intermediate forms, modular abstraction, environments, binding, representation transformations, dan program models. |
| FPL-Syntax | Syntax Analysis | Lexical/syntax analysis, grammars, parsing, parse trees/AST, parser techniques, ambiguity, error handling, dan language front-end. |
| FPL-Semantics | Compiler Semantic Analysis | Name resolution, type checking, symbol tables, scope/binding, semantic constraints, intermediate representations, dan compiler front-end validation. |
| FPL-Analysis | Program Analysis and Analyzers | Static/dynamic analysis, data/control-flow, abstract interpretation concepts, bug/security analyzers, lints, optimizations, dan correctness properties. |
| FPL-Code | Code Generation | Translation IR-to-target, instruction selection, register allocation concepts, machine code generation, optimization interfaces, dan target-specific concerns. |
| FPL-Run-Time | Runtime Behavior and Systems | Runtime services, memory management/GC, exceptions, dynamic linking, VM/JIT behavior, reflection, concurrency runtime, dan performance/security implications. |
| FPL-Constructs | Advanced Programming Constructs | Advanced abstraction/control/data constructs, metaprogramming, generics, coroutines, continuations, pattern matching, and language-specific advanced features. |
| FPL-Pragmatics | Language Pragmatics | Bagaimana fitur bahasa dipilih/digunakan dalam praktik: readability, expressiveness, safety, performance, tooling, ecosystems, dan suitability terhadap domain. |
| FPL-Formalism | Formal Semantics | Operational/denotational/axiomatic semantics, formal meaning of programs, equivalence, reasoning about execution, dan foundations for verification. |
| FPL-Methodologies | Formal Development Methodologies | Specification-to-implementation dengan metode formal, refinement, proof obligations, correctness-by-construction, dan rigorous software development. |
| FPL-Design | Design Principles of Programming Languages | Trade-off desain bahasa: abstraction, simplicity, orthogonality, safety, consistency, performance, interoperability, evolvability, dan user/programmer needs. |
| FPL-SEP | Society, Ethics, and the Profession | Dampak pilihan bahasa/toolchain terhadap safety, inclusion, accessibility, security, maintainability, licensing, sustainability, dan profesionalisme. |

## BK06 — Graphics and Interactive Techniques (`GIT`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| GIT-Fundamentals | Fundamental Concepts | Dasar grafika/interaksi: use cases, output/display, human vision, color, image formats, coordinate systems, input devices, dan risiko/abuse. |
| GIT-Visualization | Visualization | Scientific/information visualization, visual encodings, pipeline, data formats, high-dimensional data, perception/cognition, design dan evaluasi visualisasi. |
| GIT-Rendering | Applied Rendering and Techniques | Scene/object/camera/light modeling, rasterization, shaders, visibility, texture, ray methods basics, spatial structures, dan realtime rendering. |
| GIT-Modeling | Geometric Modeling | Curves/surfaces, meshes, implicit/parametric forms, volumetric/procedural/multiresolution models, reconstruction, CSG, dan spatial subdivision. |
| GIT-Shading | Shading and Advanced Rendering | Rendering equation approaches, path tracing, photon/bidirectional methods, BRDF/BSDF, shadows, subsurface, image-based/NPR/realtime techniques. |
| GIT-Animation | Computer Animation | Keyframing, interpolation, kinematics, motion capture, character/rigging, procedural animation, physics-based animation, dan timing/principles of motion. |
| GIT-Simulation | Simulation | Particle/rigid-body/cloth/fluid or related simulations, numerical integration, collisions, plausibility vs artistic control, dan interactive simulation. |
| GIT-Immersion | Immersion | VR/AR/MR/XR, spatial tracking, stereoscopy, display/input, presence, interaction, latency, safety, accessibility, dan immersive experience design. |
| GIT-Interaction | Interaction | Interactive graphics techniques, event/input models, manipulation/navigation, multimodal/haptic interaction, controllers, gesture/touch/voice, dan response feedback. |
| GIT-Image | Image Processing | Morphology, histograms, enhancement/filtering, restoration, compression/transforms, image coding, frequency-domain processing, dan links to deep learning. |
| GIT-Physical | Tangible/Physical Computing | Sensors, actuators, microcontrollers, physical interaction, CAD/CAM/fabrication, IoT connectivity, prototyping, dan safety. |
| GIT-SEP | Society, Ethics, and the Profession | Risiko dan tanggung jawab dalam graphics/media: deepfakes, IP, privacy, accessibility, bias, persuasive visuals, sustainability, dan professional practice. |

## BK07 — Human-Computer Interaction (`HCI`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| HCI-User | Understanding the User: Individual goals and interactions with others | User-centered design, needs finding, interviews/surveys/usability tests, personas, user stories, empathy/journey maps, context, stakeholders, dan human factors. |
| HCI-Accountability | Accountability and Responsibility in Design | Dampak desain terhadap sustainability, inclusivity, safety, security, privacy, harm/disparate impact, ethics, stakeholder responsibility, dan requirements. |
| HCI-Accessibility | Accessibility and Inclusive Design | Disability and inclusive design, accessibility standards, universal design, assistive technologies, inclusive frameworks, demographics, dan accessible engineering practices. |
| HCI-Evaluation | Evaluating the Design | Usability/UX evaluation, experiments, heuristic/cognitive methods, user testing, study planning, ethics/IRB, qualitative/quantitative analysis, dan validity. |
| HCI-Design | System Design | Iterative human-centered system design, interaction techniques, GUI/visual design, prototyping, design processes, hardware/software constraints, privacy, dan trade-offs. |
| HCI-SEP | Society, Ethics, and the Profession | Human values, privacy, security, fairness, trust, manipulation, accessibility, inclusivity, professional ethics, dan societal consequences of interactive systems. |

## BK08 — Mathematical and Statistical Foundations (`MSF`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| MSF-Discrete | Discrete Mathematics | Sets, relations, functions, recursion, proof, counting/combinatorics, modular arithmetic, logic, graphs, dan asymptotic/order notation. |
| MSF-Probability | Probability | Sample spaces/events, conditional probability, Bayes, random variables/distributions, expectation/variance, LLN/CLT, conditional distributions, dan computing applications. |
| MSF-Statistics | Statistics | Populations/samples, descriptive statistics, estimation/confidence intervals, correlation/regression, dimensionality reduction, statistical models, hypothesis testing, dan experimental reasoning. |
| MSF-Linear | Linear Algebra | Vectors, matrices, linear systems, transformations, geometry, eigen concepts, decompositions, least squares, dan applications in graphics/AI/data. |
| MSF-Calculus | Calculus | Limits, derivatives, integrals, series, multivariable calculus, gradients, optimization, differential equations, numerical/Monte Carlo applications, dan ML/robotics use cases. |

## BK09 — Networking and Communication (`NC`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| NC-Fundamentals | Fundamentals | Internet/network organization, switching, layering, network elements, queueing, latency/congestion, protocols, addressing, dan basic architecture. |
| NC-Applications | Networked Applications | Application-layer architectures/protocols, client-server/P2P, naming, web, messaging, streaming/services, APIs, performance, dan interaction with transport. |
| NC-Reliability | Reliability Support | Error/loss handling, retransmission, flow/congestion control, ordering, reliability semantics, fault handling, dan trade-off latency-throughput. |
| NC-Routing | Routing and Forwarding | Forwarding tables, routing algorithms/protocols, intra/inter-domain concepts, path selection, addressing/subnets, and scalability. |
| NC-SingleHop | Single Hop Communication | Link/physical-layer communication, framing, media access, LAN/WLAN concepts, switching, error detection, and local connectivity. |
| NC-Security | Network Security | Threats/attacks, cryptographic channels, TLS/VPN, secure routing/DNS, firewalls/IDS, DoS/spoofing mitigation, zero trust, monitoring, dan network defense. |
| NC-Mobility | Mobility | Cellular (4G/5G), Wi-Fi, device-to-device/IoT, ad hoc/multihop/opportunistic networks, registration/handoff, dan mobile networking trade-offs. |
| NC-Emerging | Emerging Topics | Topik frontier seperti SDN, programmable networks, middleboxes, edge, network virtualization, quantum networking, dan emerging architectures/protocols. |

## BK10 — Operating Systems (`OS`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| OS-Purpose | Role and Purpose of Operating Systems | Peran OS sebagai mediator hardware-app, universal/specialized services, design trade-offs, security/protection, system interfaces, dan evolution. |
| OS-Principles | Principles of Operating System | Kernel architectures, abstractions/resources, system calls/APIs, privilege/user-kernel modes, interrupts, isolation, performance costs, dan protection. |
| OS-Concurrency | Concurrency | Processes/threads, race conditions, synchronization, locks/semaphores/monitors, deadlock, atomicity, memory ordering, dan concurrent correctness. |
| OS-Protection | Protection and Safety | Threats/vulnerabilities, access control/authentication, isolation, protection rings, policy vs mechanism, backups/mitigations, dan OS security. |
| OS-Scheduling | Scheduling | Preemptive/non-preemptive scheduling, policies/algorithms, fairness/starvation, multiprocessor scheduling, timers, deadlines, dan trade-offs. |
| OS-Process | Process Model | Process/thread models, creation/termination, states, context switching, IPC, signals, process hierarchy, services, dan execution environments. |
| OS-Memory | Memory Management | Address spaces, allocation, paging/segmentation, virtual memory, page replacement, caching/coherence links, protection/isolation, dan performance. |
| OS-Devices | Device Management | Device drivers/interfaces, I/O scheduling, interrupts/DMA, buffering, device abstraction, performance, reliability, dan security. |
| OS-Files | File Systems API and Implementation | Files/directories, naming, APIs, metadata, allocation, free space, permissions, persistence, caching, dan basic filesystem implementation. |
| OS-Advanced-Files | Advanced File Systems | Advanced storage/filesystem concerns: journaling, distributed/parallel filesystems, snapshots, redundancy, consistency, scalability, dan recovery. |
| OS-Virtualization | Virtualization | VMs/hypervisors/containers concepts, isolation, resource virtualization, emulation, cloud links, performance, security boundaries, dan management. |
| OS-Real-time | Real-time and Embedded Systems | Timing/deadlines, deterministic response, scheduling, constrained resources, embedded OS, safety-critical considerations, dan specialized environments. |
| OS-Faults | Fault Tolerance | Failure models, redundancy, detection/recovery, checkpoints, restart, replication links, resilience, availability, dan reliable system operation. |
| OS-SEP | Society, Ethics, and the Profession | Open source/proprietary models, end-of-life, telemetry/privacy, update policy, vulnerabilities, licensing, ecosystem responsibility, dan user impacts. |

## BK11 — Parallel and Distributed Computing (`PDC`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| PDC-Programs | Programs | Parallelism/concurrency models, tasks/services, ordering/happens-before, independence, shared/distributed memory, data parallelism, cloud/cluster styles. |
| PDC-Communication | Communication | Shared memory vs message passing, channels, synchronization-through-communication, collective operations, network/service APIs, latency/bandwidth, dan failure. |
| PDC-Coordination | Coordination | Synchronization, mutual exclusion, consistency, consensus/coordination, transactions, deadlock/livelock, ordering, and distributed coordination protocols. |
| PDC-Evaluation | Evaluation | Correctness and performance evaluation, scalability, speedup/efficiency, Amdahl/USL concepts, latency/throughput, energy, fault/adversarial behavior, dan tools. |
| PDC-Algorithms | Algorithms | Parallel/distributed algorithms for linear algebra, data processing, graphs/search, simulation, load balancing, partitioning, map-reduce styles, and domain patterns. |

## BK12 — Software Development Fundamentals (`SDF`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| SDF-Fundamentals | Fundamental Programming Concepts and Practices | Variables/types/expressions, I/O, control flow, functions, modularity, APIs/libraries, classes, recursion, exceptions, file I/O, reading/tracing/documenting programs. |
| SDF-Data-Structures | Fundamental Data Structures | Language/library data structures, arrays/lists, stacks/queues, sets/maps/dictionaries, trees, choosing structures, operations, dan effective use. |
| SDF-Algorithms | Algorithms | Fundamental algorithms, searching/sorting/basic problem-solving, algorithm selection, efficiency awareness, implementation correctness, dan relation to AL. |
| SDF-Practices | Software Development Practices | Testing/debugging, readable/maintainable code, IDE/tooling, version control basics, defensive/security mindset, documentation, dan modern coding workflow. |
| SDF-SEP | Society, Ethics, and the Profession | Etika pemrograman, professional values, responsibility to users/society, security mindset, accessibility, licensing, dan consequences of code. |

## BK13 — Software Engineering (`SE`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| SE-Teamwork | Teamwork | Communication/collaboration, conflict resolution, pair/swarming/code review, version-control collaboration, team roles, inclusive culture, stakeholder interfaces, distributed teams. |
| SE-Tools | Tools and Environments | Version/configuration control, reproducible builds, branching, IDEs, static/dynamic analysis, CI/CD concepts, requirements/design/testing tools, dan toolchain selection. |
| SE-Requirements | Product Requirements | Functional/non-functional requirements, elicitation, user stories/use cases, quality attributes, feasibility/consistency, risk, stakeholders, prototyping, dan prioritization. |
| SE-Design | Software Design | Architecture and detailed design, abstraction/separation of concerns/information hiding, APIs, components, patterns, modularity, dependencies, quality attributes, dan trade-offs. |
| SE-Construction | Software Construction | Coding practices, testing while constructing, TDD, code style, review, dependency management, secure coding, prioritization, and production-oriented implementation. |
| SE-Validation | Software Verification and Validation | Testing strategy, unit/integration/system tests, test quality, failure modes, coverage, static/dynamic verification, validation against requirements, dan automation. |
| SE-Refactoring | Refactoring and Code Evolution | Code health, refactoring, maintenance, backward compatibility, version/schema/API evolution, technical debt, migration, and tool-assisted change. |
| SE-Reliability | Software Reliability | Failure/error models, robustness, redundancy, fault tolerance, availability, observability, recovery, error handling, and reliability engineering. |
| SE-Formal | Formal Methods | Formal specification, logic/proofs, model checking/verification concepts, invariants, contracts, correctness reasoning, dan mathematically rigorous assurance. |

## BK14 — Security (`SEC`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| SEC-Foundations | Foundational Security | CIA/risk/security mindset, authn/authz, threats/vulnerabilities/attack surfaces, DoS, least privilege, defense in depth, zero trust, privacy/performance trade-offs. |
| SEC-SEP | Society, Ethics, and the Profession | Security/privacy responsibilities, responsible disclosure, harms, laws/policy context, ethics of offensive/defensive work, trust, dan professional conduct. |
| SEC-Coding | Secure Coding | Input validation, injection, memory safety, secure APIs, error handling, secrets, least privilege, dependency risks, defensive coding, testing, dan vulnerability prevention. |
| SEC-Crypto | Cryptography | Symmetric/asymmetric cryptography, hashing/MAC, signatures, key exchange/management, protocols, randomness, PKI, limitations, and correct use of primitives. |
| SEC-Engineering | Security Analysis, Design, and Engineering | Threat modeling, requirements/controls, attack surface analysis, secure architecture, privacy-by-design, adversarial analysis, testing/attestation, dan cyber-physical security. |
| SEC-Forensics | Digital Forensics | Evidence acquisition/preservation, logs/artifacts, timelines, disk/memory/network forensics concepts, chain of custody, analysis, reporting, dan legal/ethical boundaries. |
| SEC-Governance | Security Governance | Assets/risk, governance vs management/control, policies, compliance, data lifecycle/backup/retention, cloud risks, breach disclosure, dan organizational security. |

## BK15 — Society, Ethics, and the Profession (`SEP`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| SEP-Context | Social Context | Hubungan computing dengan masyarakat, power/stakeholders, benefits/harms, global/cultural context, digital divides, unintended consequences, dan public good. |
| SEP-Ethical-Analysis | Methods for Ethical Analysis | Framework dan metode analisis etika, stakeholder/impact analysis, competing values, ethical reasoning, case analysis, dan decision justification. |
| SEP-Professional-Ethics | Professional Ethics | Codes of ethics, professional responsibility, competence, honesty, accountability, conflicts of interest, whistleblowing, dan public interest. |
| SEP-IP | Intellectual Property | Copyright, patents, trademarks, trade secrets, licensing, open source, fair use, ownership, attribution, dan software/data/content IP issues. |
| SEP-Privacy | Privacy and Civil Liberties | Privacy principles, surveillance, consent, data minimization, civil liberties, anonymity, profiling, privacy law/policy, dan privacy-by-design. |
| SEP-Communication | Communication | Technical/nontechnical communication, documentation, presentation, stakeholder communication, accessibility, respectful collaboration, dan communicating uncertainty/risks. |
| SEP-Sustainability | Sustainability | Energy/resource use, carbon/material impacts, lifecycle/e-waste, sustainable design/operations, trade-offs, environmental justice, dan responsible computing. |
| SEP-History | Computing History | Perkembangan hardware/software/networking/mobile/cloud/AI, tokoh/organisasi, historical context, diverse perspectives, and lessons shaping present/future. |
| SEP-Economies | Economies of Computing | Business/economic models, attention/data economies, labor/automation, digital platforms, subscription/freemium, market power, digital divide, dan societal effects. |
| SEP-Security | Security Policies, Laws and Computer Crimes | Computer crime, cyber law/policy, security regulation, unauthorized access/fraud/abuse, incident responsibilities, enforcement, dan social/legal context. |
| SEP-DEIA | Diversity, Equity, Inclusion, and Accessibility | DEIA in computing teams/products, bias/exclusion, accessibility, representation, inclusive design, equitable impacts, and culturally responsive professional practice. |

## BK16 — Systems Fundamentals (`SF`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| SF-Overview | Overview of Computer Systems | Pandangan end-to-end sistem komputer: layers/components, hardware-software interaction, execution, storage, communication, abstractions, dan system context. |
| SF-Foundations | Basic Concepts | Fundamental system concepts seperti state, concurrency, caching, locality, naming, indirection, virtualization, fault, layering, interface, dan abstraction. |
| SF-Resource | Resource Management | Allocation/scheduling/accounting resources: CPU, memory, storage, network, energy; contention, fairness, quotas, utilization, dan policy/mechanism. |
| SF-Performance | System Performance | Latency, throughput, bottlenecks, locality/caching, concurrency, capacity, scalability, efficiency, workload effects, dan performance trade-offs. |
| SF-Evaluation | Performance Evaluation | Measurement, benchmarking, experiments, profiling, modeling, statistical interpretation, workload selection, repeatability, dan capacity/scalability evaluation. |
| SF-Reliability | System Reliability | Fault/failure models, redundancy, recovery, availability, durability, replication/checkpointing links, observability, and resilient system design. |
| SF-Security | System Security | System-level threat boundaries, isolation, authentication/authorization links, secure interfaces, attack surfaces, defense-in-depth, dan security-performance trade-offs. |
| SF-Design | System Design | System decomposition, interfaces, modularity, abstraction, non-functional requirements, performance/reliability/security trade-offs, scalability, dan architectural reasoning. |
| SF-SEP | Society, Ethics, and the Profession | System-scale impacts: reliability/safety obligations, privacy/security, sustainability, accessibility, responsible operation, risk communication, dan professional accountability. |

## BK17 — Specialized Platform Development (`SPD`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| SPD-Common | Common Aspects/Shared Concerns | Cross-platform concerns: lifecycle, deployment, APIs, data/storage, networking, security/privacy, UI, performance/energy, testing, portability, dan platform constraints. |
| SPD-Web | Web Platforms | Web architecture, browser/server, HTTP/web APIs, frontend/backend concepts, state/storage, security, accessibility, performance, deployment, dan web standards. |
| SPD-Mobile | Mobile Platforms | Mobile OS/app lifecycle, touch/sensors/location, constrained resources/energy, offline/sync, permissions/privacy, app distribution, responsive UX, dan network variability. |
| SPD-Robot | Robot Platforms | Robot hardware/software platforms, sensors/actuators, middleware, realtime/control integration, autonomy interfaces, safety, deployment, dan testing. |
| SPD-Embedded | Embedded Platforms | Microcontrollers/SoCs, constrained compute/memory/energy, firmware, interrupts/I/O, realtime, sensors/actuators, communication, reliability, dan safety. |
| SPD-Game | Game Platforms | Game loops/engines, rendering/physics/audio/input, assets, scripting, multiplayer/networking, performance, platform constraints, deployment, dan player experience. |
| SPD-Interactive | Interactive Computing Platforms | Interactive/physical/XR/IoT-like platforms, multimodal input/output, sensors, haptics, fabrication links, latency, connectivity, and human-centered interaction. |
| SPD-SEP | Platform-Specific Society, Ethics, and the Profession | Isu SEP lintas web/mobile/game/robotics/interactive: privacy, accessibility, persuasive design, safety, security, IP, platform power, sustainability, dan responsible deployment. |

## APTIKOM Additional BK from CC2020 — Main CS2023 Absorption (`Existing APTIKOM Code`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| Coverage Assessment | Recommendation | Risk if Removed Blindly |

## Programming Fundamentals — SDF-Fundamentals; SDF-Data-Structures; SDF-Algorithms; SDF-Practices; AL-Foundational; FPL-OOP (`BK14`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| Very high / effectively absorbed in CS2023 | Tidak perlu BK tersendiri jika 17 KA CS2023 dipakai sebagai canonical taxonomy. | Risiko rendah selama semua KU SDF/AL/FPL yang relevan benar-benar dipetakan ke MK pemrograman. |

## User Experience Design — HCI-User; HCI-Accountability; HCI-Accessibility; HCI-Evaluation; HCI-Design; GIT-Interaction (`BK04`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| Very high / HCI CS2023 lebih lengkap daripada label UX semata | Tidak perlu BK tersendiri; jadikan UX sebagai cluster/sub-BK atau course packaging di bawah HCI. | Risiko rendah; pastikan user research, accessibility, evaluation, visual/interaction design tetap eksplisit. |

## Project Management — SE-Teamwork; SE-Tools; SE-Requirements; SE-Design; SE-Construction; SE-Validation; SE-Refactoring; SE-Reliability; SEP-Communication; SEP-Professional-Ethics (`BK03`)

| Kode KU | Knowledge Unit | Deskripsi |
|---|---|---|
| Substantial for software project execution, but not identical to classical PM body of knowledge | Tidak perlu BK terpisah untuk taxonomy CS2023-only; embed engineering/project execution in SE. Jika CPL/profil lulusan butuh scope-cost-schedule-procurement/leadership, tambahkan sebagai local overlay/sub-BK. | Risiko sedang: CS2023 SE secara eksplisit mengurangi fokus pada team leadership/project management; domain PM klasik bisa kurang jika dihapus tanpa mapping. |

---

*"Problem Solvers in Digital, Driven by Ethics and Islamic Values"* — Program Studi Informatika, Universitas Al Azhar Indonesia
