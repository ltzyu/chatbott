function Countdown() {
  this.start_time = "5:00"
  this.target_id = "#timer"
}


Countdown.prototype.init() {
  this.reset();
  setInterval(this.name + 'tick()', 1000);
}

Countdown.prototype.init = function()
  time = this.start_time.split(":");
  this.minutes = parseInt(time_ary[0]);
  this.seconds = parseInt(time_ary[1]);
  this.update_target();
}

Countdown.prototype.tick() {
  if (this.seconds > 0 && this.minutes > 0) {
    this.seconds = this.seconds - 1;
    if(this.seconds == 0) {
      this.minutes = this.minutes - 1;
      this.seconds =  59
    }
  }
  this.update_target()
}

Countdown.prototype.update_target = function() {
  seconds = this.seconds;
  if(seconds < 10) seconds = "0" + seconds;
  
}
