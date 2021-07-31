public class Seat {
    //예약자 이름
    private String name;

    public String getName() {
        return name;
    }

    public void reserve(String name){
        this.name = name;
    }

    public void cancel(){
        this.name =null;
    }

    public boolean isOccupied(){
//        if(name!= null) return true;
//        else return false;
        return name != null;
    }

    public boolean match(String checkName){
//        if(name.equals(checkName)) return true;
//        else return false;
        return name.equals(checkName);
    }
}
