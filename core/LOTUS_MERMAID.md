flowchart TD
    %% Noder
    subgraph NODE["Node Layer"]
        direction TB
        NL[Node LOTUS Panel]:::lotus
        N1[Baseline Violation Detected]:::baseline
        N2[Node Self-Correction]:::action
        N3[Surplus > 2× Baseline?]:::action
        N4[Local Redistribute / Voluntary Window]:::action
        N5[Node Report to Regional LOTUS]:::report
    end

    subgraph REGIONAL["Regional Layer"]
        direction TB
        RL[Regional LOTUS Panel]:::lotus
        R1[Regional Recovery Triggered]:::action
        R2[Redistribute Regional Surplus / Emergency Pools]:::action
        R3[Report to Global LOTUS]:::report
        R4[Review Node Amendments / Proposals]:::proposal
    end

    subgraph GLOBAL["Global Layer"]
        direction TB
        GL[Global LOTUS Panel]:::lotus
        G1[Global Recovery Trigger]:::action
        G2[Approve/Reject Baseline Amendments]:::proposal
        G3[Global Surplus Audit & Redistribution]:::action
        G4[Structural / Emergency Override]:::critical
    end

    %% Baseline Recovery Connections
    N1 --> N2 --> N5 --> R1 --> R2 --> R3 --> G1
    %% Surplus Flow Connections
    N3 --> N4 --> R2
    R3 --> G3
    %% Baseline Amendments
    R4 --> G2
    %% Emergency / Override
    N1 --> GL
    R1 --> GL
    G4 --> N2
    G4 --> R2

    %% Styling
    classDef lotus fill:#ffd966,stroke:#b58900,stroke-width:2px,color:#000,font-weight:bold;
    classDef action fill:#66ccff,stroke:#006699,stroke-width:2px,color:#000;
    classDef baseline fill:#ff6666,stroke:#900,stroke-width:2px,color:#fff;
    classDef proposal fill:#cce0ff,stroke:#004080,stroke-width:2px,color:#000;
    classDef report fill:#d4f8d4,stroke:#006600,stroke-width:2px,color:#000;
    classDef critical fill:#ff0000,stroke:#660000,stroke-width:3px,color:#fff;