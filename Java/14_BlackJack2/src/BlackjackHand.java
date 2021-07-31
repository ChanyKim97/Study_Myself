public class BlackjackHand extends Deck<BlackjackCard>{

    public int getValue(){
//        int sum = 0;
//
//        for(Card a : cards){
//            switch (a.getRank()) {
//                case "Jack":
//                case "Queen":
//                case "King":
//                    sum += 10;
//                    break;
//                case "Ace":
//                    if (11 + sum > 21) sum += 1;
//                    else sum += 11;
//                    break;
//                default:
//                    sum += Integer.parseInt(a.getRank());
//                    break;
//            }
//        }
//
//        return sum;
        int sum=0;

        for(BlackjackCard card : getCards()){
            //BlackjackCard card = (BlackjackCard) a;

            if(card.isAce()) {
                if (sum + card.getValue() > 21) {
                    sum += 1;
                }
                else sum += card.getValue();
            }
            else sum += card.getValue();
        }

        return sum;
    }

    public boolean isBusted(){
        return getValue() > 21;
    }

    public boolean isBlackjack(){
        if(getCards().size() == 2 && getValue() == 21) return true;
        else return false;
    }
}
