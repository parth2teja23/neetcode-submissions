class LinkedList {
    int val;
    LinkedList next;

    public LinkedList() {
        this.val = 0;
        this.next = null;
    }

    public int get(int index) {
    LinkedList temp = this.next;
    for (int i = 0; i < index; i++){
        if (temp == null) return -1;
        temp = temp.next;
    }
    return temp == null ? -1 : temp.val;
}

public void insertHead(int val) {
    LinkedList newNode = new LinkedList();
    newNode.val = val;
    newNode.next = this.next;
    this.next = newNode;
}
    public void insertTail(int val) {
        LinkedList temp = this;
        while (temp.next != null){
            temp = temp.next;

        }
        LinkedList next = new LinkedList();
        next.val = val;
        next.next = null;
        temp.next = next;
    }

public boolean remove(int index) {
    LinkedList temp = this;
    for (int i = 0; i < index; i++){
        if (temp.next == null) return false;
        temp = temp.next;
    }
    if (temp.next == null) return false;
    temp.next = temp.next.next;
    return true;
}

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> res = new ArrayList<>();
        LinkedList temp = this.next;

        while (temp != null){
            res.add(temp.val);
            temp = temp.next;
        } 
        return res;
    }
}
