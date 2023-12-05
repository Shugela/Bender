import { game } from './game.js';


// get canvas and canvas context to draw on it
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");




function initialization(){
    let player = new player('Shugema')
    let game = new game(30);
    return { player, game }
}

function draw(){

}

function update(){

}

function gameloop(){
    update();
    draw();
}

function main(){
    initialization()

}


gameloop()