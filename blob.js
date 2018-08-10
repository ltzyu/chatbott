function Blob(x, y, r) {
  this.pos = createVector(x, y);
  this.r = r;
  this.vel = createVector(0, 0);

  var yoff = 0;
  this.update = function() {
    var newvel = createVector(mouseX - width / 2, mouseY - height / 2);
    newvel.div(50);
    //newvel.setMag(3);
    newvel.limit(3);
    this.vel.lerp(newvel, 0.2);
    this.pos.add(this.vel);
  }

  this.eats = function(other) {
    var d = p5.Vector.dist(this.pos, other.pos);
    if (d < this.r + other.r) {
      var sum = PI * this.r * this.r + PI * other.r * other.r;
      this.r = sqrt(sum / PI);
      //this.r += other.r
      return true;
    } else {
      return false;
    }
  }
  this.constrain = function() {
    blob.pos.x = constrain(blob.pos.s, -width / 4, width / 4);
    blob.pos.y = constrain(blob.pos.y, -height / 4, height / 4)
  }
  this.show = function() {
    push();
    translate(this.pos.x, this.pos.y);
    beginShape();
    var xoff = 0;
    for (var a = 0; a < TWO_PI; a += 0.1) {
      var offset = map(noise(xoff + yoff)), 0, 1, -25, 25);
      var r = this.r + random(-5, 5)
      var x = this.r * cos(a);
      var y = this.r * sin(a);
      vertex(x, y);
      xoff += 0.1;
      //ellipse(x, y, 4, 4)
    }
    endShape();
    pop();

    yoff += 0.01;
  }
}
