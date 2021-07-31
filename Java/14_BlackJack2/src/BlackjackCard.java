public class BlackjackCard extends Card{
    public BlackjackCard(int suitNumber, int rankNumber) {
        super(suitNumber, rankNumber);
    }

    public int getValue(){
        switch (getRank()){
            case "Ace":
                return 11;
            case "Jack":
            case "Queen":
            case "King":
                return 10;
            default:
                return Integer.parseInt(getRank());
        }
    }

    public boolean isAce(){
        if(rankNumber == 1) return true;
        else return false;
        //이것도 합쳐서 표현할것
    }
}
