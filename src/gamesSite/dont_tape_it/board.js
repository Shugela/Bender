import { rectangle } from "./rectangle";

class Board {

    constructor(x, y){
        this.pos_x = x;
        this.pos_y = y;
        this.array = new Array(this.y)
    }   

    newBoard(){
        let a = 700/3
        for(var y=0; y<this.pos_y; y++){
            this.array[y] = new Array(this.pos_x)
            for(var x=0; x<this.pos_x; x++){
                this.array[y][x] = new rectangle(a, a, y*a, x*a)
            }
        }
    }
}