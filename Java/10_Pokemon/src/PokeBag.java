import java.util.ArrayList;
import java.util.HashMap;

public class PokeBag {
    private final HashMap<String, ArrayList<Pokemon>> pokemons = new HashMap<>();

    public ArrayList<Pokemon> getPokemons(String name) {
        return pokemons.get(name);
    }

    public void add(Pokemon pokemon) {
        if(getPokemons(pokemon.name) == null){
            pokemons.put(pokemon.name, new ArrayList<Pokemon>());
        }
        getPokemons(pokemon.name).add(pokemon);
    }

    public Pokemon getStrongest(String name) {
        ArrayList<Pokemon> templist = new ArrayList<>();
        templist = getPokemons(name);

        if(templist == null) return null;
        int maxcp=0;
        Pokemon Strongest = null;
        for(Pokemon a : templist){
            if(a.cp>maxcp) {
                maxcp = a.cp;
                Strongest = a;
            }
        }

        return Strongest;
    }

    public Pokemon getStrongest() {
        Pokemon Strongest =null;

        int maxcp=0;
        for(String a : pokemons.keySet()){
            if(getStrongest(a).cp > maxcp){
                maxcp = getStrongest(a).cp;
                Strongest = getStrongest(a);
            }
        }
        return Strongest;
    }
}