public class Person {
    private String name;
    private int age;
    private int cashAmount;
    private BankAccount account;

    public Person(String pName, int pAge){
        name = pName;
        if(pAge < 0) age = 12;
        else age = pAge;
        cashAmount = 0;
    }

    public Person(String pName, int pAge, int pCashAmount){
        name = pName;
        if(pAge < 0) age = 12;
        else age = pAge;
        if(pCashAmount<0) cashAmount = 0;
        else cashAmount = pCashAmount;
    }

    public void setAge(int newAge){
        if(newAge>=0) {
            age = newAge;
        }
    }

    public int getAge(){
        return age;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getName(){
        return name;
    }

    public void setCashAmount(int newCash){
        if(newCash>=0){
            cashAmount = newCash;
        }
    }

    public int getCashAmount(){
        return cashAmount;
    }

    public void setAccount(BankAccount newaccount){
        account = newaccount;
    }

    public BankAccount getAccount(){
        return account;
    }

    public boolean transfer(Person to, int amount) {
        // insert code here
        if(amount < 0 || amount > account.getBalance()){
            System.out.println("false - from: "+name+", to: "+to.getName()+", amount: "+ amount +", balance: "+ account.getBalance());
            return false;
        }
        account.setBalance(account.getBalance() - amount);
        to.getAccount().setBalance(to.getAccount().getBalance() + amount);
        System.out.println("true - from: "+name+", to: "+to.getName()+", amount: "+ amount +", balance: "+ account.getBalance());
        return true;
    }

    public boolean transfer(BankAccount to, int amount){
        if(amount < 0 || amount > account.getBalance()){
            System.out.println("false - from: "+name+", to: "+to.getOwner().getName()+", amount: "+ amount +", balance: "+ account.getBalance());
            return false;
        }
        account.setBalance(account.getBalance() - amount);
        to.setBalance(to.getBalance() + amount);
        System.out.println("true - from: "+name+", to: "+to.getOwner().getName()+", amount: "+ amount +", balance: "+ account.getBalance());
        return true;
    }
}