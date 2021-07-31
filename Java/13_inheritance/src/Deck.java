import java.util.ArrayList;
import java.util.Random;

public class Deck {
    private ArrayList<Card> cards = new ArrayList<>();
    //private ArrayList<Card> hand = new ArrayList<>();

    public ArrayList<Card> getCards(){
        return cards;
    }

    public void addCard(Card card){
        cards.add(card);
    }

    public void print(){
        for(Card a : cards){
            System.out.println(a);
        }
    }

    public void shuffle(){
        Random a = new Random();

        for(int i =0; i<cards.size(); i++){
            int randomindex = a.nextInt(cards.size());
            Card temp = cards.get(i);
            cards.set(i, cards.get(randomindex));
            cards.set(randomindex, temp);
        }
    }

    public Deck deal(int count){
        Deck hand = new Deck();

        for(int i = 0; i<count; i++){
//            hand.addCard(cards.get(cards.size()-1));
//            cards.remove(cards.size()-1);
            //이부분 합쳐서 표현이 가능함
            hand.addCard(cards.remove(cards.size()-1));
        }
        return hand;
    }
}
