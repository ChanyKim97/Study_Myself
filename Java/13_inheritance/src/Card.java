public class Card {
    public final int suitNumber;
    public final int rankNumber;

    public Card(int suitNumber, int rankNumber){
        this.suitNumber = suitNumber;
        this.rankNumber = rankNumber;
    }

    public String getSuit(){
        switch (suitNumber){
            case 1:
                return "Clubs";
            case 2:
                return "Hearts";
            case 3:
                return "Diamonds";
            case 4:
                return "Spades";
        }
        return null;
    }

    public String getRank(){
        if(rankNumber == 1) return "Ace";
        else if(rankNumber == 11) return "Jack";
        else if(rankNumber == 12) return "Queen";
        else if(rankNumber == 13) return "King";
        else return String.valueOf(rankNumber);
    }

    public String toString(){
        return getRank() + " of " + getSuit();
    }
}
