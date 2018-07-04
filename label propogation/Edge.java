/**
 * Created by mitta on 01-Jan-18.
 */
public class Edge {

    public Node n1 , n2;
    public String id;
    public int df;

    public Edge(Node n1, Node n2, String id) {
        this.n1 = n1;
        this.n2 = n2;
        this.id = id;
    }

    public Edge(Node n1, Node n2){
        this(n1, n2, getId(n1, n2));
    }

    public static String getId(Node n1, Node n2) {
        if(n1.get_id()<n2.get_id()) {
            return Integer.toString(n1.get_id()) + "_" + Integer.toString(n2.get_id());
        }
        return Integer.toString(n2.get_id())+"_"+Integer.toString(n1.get_id());
    }


}
