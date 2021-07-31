public class BankAccount {
    private int balance;    //잔액
    private Person owner;   //주인

    public BankAccount(int pBalance) {
        if(pBalance<0) balance = 0;
        else balance = pBalance;
    }

    public BankAccount(Person pOwner) {
        balance = 0;
        owner = pOwner;
    }

    public BankAccount(int pBalance, Person pOwner) {
        if(pBalance<0) balance = 0;
        else balance = pBalance;
        owner = pOwner;
    }

    public void setBalance(int newbalance){
        balance = newbalance;
    }

    public int getBalance(){
        return balance;
    }

    public void setOwner(Person newowner){
        owner = newowner;
    }

    public Person getOwner() {
        return owner;
    }

    //입금 메소드
    boolean deposit(int amount){
        if(owner.getCashAmount() < amount || amount < 0){
            System.out.println("입금 실패입니다. 잔고: "+ balance + "원, 현금: "+owner.getCashAmount() +"원");
            return false;
        }
        else{
            balance += amount;
//            owner.cashAmount -= amount;
            owner.setCashAmount(owner.getCashAmount()-amount);
            System.out.println(amount +"원 입금하였습니다. 잔고: "+ balance + "원, 현금: "+owner.getCashAmount() +"원");
            return true;
        }
    }

    //외화입금을통한 polymorphism 공부
    public boolean deposit(double amount, double exchangeRate){
        return deposit((int) (amount*exchangeRate));
    }

    //출금 메소드
    boolean withdraw(int amount){
        if(amount <0 || amount > balance){
            System.out.println("출금 실패입니다. 잔고: "+ balance + "원, 현금: "+owner.getCashAmount() +"원");
            return false;
        }
        else{
            balance -= amount;
//            owner.cashAmount += amount;
            owner.setCashAmount(owner.getCashAmount()+amount);
            System.out.println(amount +"원 출금하였습니다. 잔고: "+ balance + "원, 현금: "+owner.getCashAmount() +"원");
            return true;
        }
    }

    //계좌이체 메소드
    //받는사람, 이체금액 -> 성공여부
    public boolean transfer(Person to, int amount) {
        // insert code here
        if(amount < 0 || amount > balance){
            System.out.println("false - from: "+owner.getName()+", to: "+to.getName()+", amount: "+ amount +", balance: "+ balance);
            return false;
        }
        balance -= amount;
        to.getAccount().setBalance(to.getAccount().getBalance() + amount);
        System.out.println("true - from: "+owner.getName()+", to: "+to.getName()+", amount: "+ amount +", balance: "+ balance);
        return true;
    }

    public boolean transfer(BankAccount to, int amount){
        if(amount < 0 || amount > balance){
            System.out.println("false - from: "+owner.getName()+", to: "+to.owner.getName()+", amount: "+ amount +", balance: "+ balance);
            return false;
        }
        balance -= amount;
//        to.setBalance(to.getBalance() + amount);
        to.balance += amount; // 같은 클래스 안에서는 private에 접근할 수있음을 생각해야함
        System.out.println("true - from: "+owner.getName()+", to: "+to.owner.getName()+", amount: "+ amount +", balance: "+ balance);
        return true;
    }
}
