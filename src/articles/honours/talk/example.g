RequirePackage("gasp");
config := PointConfiguration(0,0,300,300);
propose := CreateSimpleFlipPropose(1/2);
check := CreateStraussCheck(1/900, 9/10, 15);
GUISimulate(config, "Strauss", 300, 300, propose, check);
