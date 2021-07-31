import java.util.HashMap;

public class Main {
    public static void main(String[] args){
        HashMap<String, Pokemon> pokemondogam= new HashMap<>();

        pokemondogam.put("피카츄", new Pokemon("라이츄"));
        pokemondogam.put("파이리", new Pokemon("리자몽"));

        Pokemon pika = pokemondogam.get("피카츄");

        for(String key : pokemondogam.keySet()){
            System.out.println(pokemondogam.get(key));
        }
    }
}
