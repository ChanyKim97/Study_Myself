public class Box<T> {
    private T something;

    public void set(T object) {
        this.something = object;
    }

    public T get() {
        return something;
    }
}
