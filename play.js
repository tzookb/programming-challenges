// Debug your banana constructor here. Run the test cases first to see the test feedback.
function Banana = (length, diameter) => {
  this.color = 'yellow';
  this.length = length;
  this.diameter = diameter;
  this.isYummy = true
  this.rot = function() {
   this.isYummy = false;
  };
 }