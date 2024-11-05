function givealert() {  //i next to the heading
    alert("Please Enter details as they are in the LFT (Liver Function Test)");
}
function givealert1() {  //i next to the analysis result
    alert("LivCheck is mostly accurate, but can have a 20% chance of being wrong. So no matter what the ouput, it's always advisable to visit a doctor!");
}
function validateGenderInput(input) { //Gender should be only 0 or 1
const value = input.value;
if (value !== "0" && value !== "1") {
    input.setCustomValidity("Please enter 0 for Female or 1 for Male.");
} else {
    input.setCustomValidity(""); 
}
}