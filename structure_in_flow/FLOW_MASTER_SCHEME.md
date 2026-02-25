%% FLOW – Radial Spiral Map with Nodes & Satellites
flowchart TD
    %% CENTRAL FLOW SPIRAL
    IND[Individual]
    IND --> MC[Micro-Circle<br>2-5 people]
    MC --> BC[Baseline Circle<br>10-30 people]
    BC --> FN[Flow Node<br>30+ people]

    %% FLOW NODE SATELLITES (Radial/Circular)
    FN --> PT[Professional Team]
    FN --> VT[Volunteer/Research Team]
    FN --> LY[Lyceum Musaeum]
    FN --> BL[Baseline Resource Access]

    %% Simulate circular layout by connecting satellites in a loop
    PT -.-> VT
    VT -.-> LY
    LY -.-> BL
    BL -.-> PT

    %% INTER-NODE CONNECTIONS
    FN --- FN2[Flow Node B]
    FN --- FN3[Flow Node C]

    BL --- BL2[Baseline B]
    BL2 --- BL3[Baseline C]
    BL3 --- BL

    PT --- PT2[Professional B]
    PT2 --- PT3[Professional C]
    PT3 --- PT

    LY --- LY2[Lyceum B]
    LY2 --- LY3[Lyceum C]
    LY3 --- LY

    %% REGIONAL & GLOBAL LAYERS
    FN --> REG[Regional Network<br>3-10 Nodes]
    REG --> GLOB[Global Flow Network<br>Multiple Regions]

    %% COLOR CLASSES (BLACK TEXT)
    classDef individual fill:#e0f7fa,stroke:#00796b,stroke-width:2px,color:#000;
    classDef circle fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,color:#000;
    classDef node fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#000;
    classDef team fill:#bbdefb,stroke:#1976d2,stroke-width:2px,color:#000;
    classDef lyceum fill:#d1c4e9,stroke:#512da8,stroke-width:2px,color:#000;
    classDef baseline fill:#ffcdd2,stroke:#c62828,stroke-width:2px,color:#000;
    classDef network fill:#ffe0b2,stroke:#ef6c00,stroke-width:2px,color:#000;

    %% ASSIGN CLASSES
    class IND individual;
    class MC,BC circle;
    class FN,FN2,FN3 node;
    class PT,PT2,PT3,VT team;
    class LY,LY2,LY3 lyceum;
    class BL,BL2,BL3 baseline;
    class REG,GLOB network;

    %% STYLE ARROWS & NODES
    style IND stroke:#000,stroke-width:2px
    style MC stroke:#000,stroke-width:2px
    style BC stroke:#000,stroke-width:2px
    style FN stroke:#000,stroke-width:2px
    style REG stroke:#000,stroke-width:2px
    style GLOB stroke:#000,stroke-width:2px