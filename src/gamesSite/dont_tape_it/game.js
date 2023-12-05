export class game {

    constructor(timer){
        this.timer = timer;
        this.gameState = false;
    }

    set setGameState(bool){
        this.gameState = bool;
    }

    get getGameState(){
        return this.gameState;
    }
}