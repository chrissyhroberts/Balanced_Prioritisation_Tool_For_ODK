module pawn(){ 

difference(){
union(){
//crosspiece on base    
translate([0,0,1.5])rotate(0,0,0)cube([3,50,3],center=true);    
translate([0,0,1.5])rotate(60,0,0)cube([3,50,3],center=true);   
translate([0,0,1.5])rotate(120,0,0)cube([3,50,3],center=true);   

//main body pawn
difference(){    
cylinder(d1=12,d2=30,h=50,$fn=6);
translate([0,0,49])cylinder(d1=28,d2=28,h=1,$fn=6);

}
// ring on base
difference(){
    cylinder(d=51,h=3,$fn=60);
    cylinder(d=45,h=3,$fn=60);
}

  
}


}
//question mark
translate([-7.5,-10,49])linear_extrude(height=1)text("?",size=20);

}

module question(){ 
difference(){
    

translate([0,0,49])cylinder(d=28,d2=28,h=1,$fn=6);
translate([-7.5,-10,49])linear_extrude(height=1)text("?",size=20);

}

difference(){
    translate([0,0,3])cylinder(d=51,h=1,$fn=60);
    translate([0,0,3])cylinder(d=45,h=1,$fn=60);
}
    translate([0,0,3.5])rotate(0,0,0)cube([3,50,1],center=true);    
    translate([0,0,3.5])rotate(60,0,0)cube([3,50,1],center=true);   
    translate([0,0,3.5])rotate(120,0,0)cube([3,50,1],center=true);   

}



color("white")pawn();
//color("black")question();
