class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.current_track = None  # <--- New Control Pointer
    
    def show_current_track(self):
        if self.current_track is None:
            print("Current Track: Playlist is empty")
            return
        print(f" -->> Now Playing: '{self.current_track.data}'")
    
    def next_track(self):
        if self.head is None:
            print(" -> Error: empty playlist")
            return
        
        self.current_track = self.current_track.next
    
    def prev_track(self):
        if self.head is None:
            print(" -> Error: empty playlist")
            return
        
        self.current_track = self.current_track.prev

    def insert_at_end(self, new_data):
        new_node = Node(new_data)  # New node

        if self.head is None:
            # sets the head and tail
            self.head = new_node
            self.tail = new_node

            # FIX: Connects next and prev to the node itself (circular)
            new_node.next = new_node 
            new_node.prev = new_node 
            
            print(f" -> Added {new_data} in an empty list")

            self.current_track = new_node  # <--- Critical: Set the current track!
        else:
            # ---Logic---
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail

            self.current_track = new_node
            print(f" -> Added {new_data} at the end of the circular list")

        # increment size
        self.size += 1

    def insert_at_start(self, new_data):
        new_node = Node(new_data)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node
            
            # FIX: Connects next and prev to the node itself (circular)
            new_node.prev = new_node
            new_node.next = new_node
            
            print(f" -> Added '{new_data}' in an empty list")
            self.current_track = new_node # Set current track for empty list

        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
            print(f" -> Added {new_data} at the start of the circular list")
            
        self.size += 1

    def insert_after_node(self, data, target_data):
        # Check for empty list
        if self.head is None:
            print(" -> Error: list empty")
            return
        
        # Initialize Variables
        target_node = self.head
        found = False

        # Search for Target Node
        while True:
            if target_node.data == target_data:
                found = True
                break

            target_node = target_node.next

            # Stop search when we loop back to head
            if target_node == self.head:
                break
        
        # Handle Search Result
        if not found:
            print(" -> Error: target data not found")
            return
        
        # Check Edge Case: Inserting after the tail
        if target_node == self.tail:
            # Re-use insert_at_end logic
            self.insert_at_end(data)
            # The insert_at_end method already handles the printing and size increment
            return
        
        # Insert in the middle
        new_node = Node(data)
        node_after_target = target_node.next

        # Link new node
        new_node.next = node_after_target
        new_node.prev = target_node

        # Link neighbors
        node_after_target.prev = new_node
        target_node.next = new_node
        
        print(f" -> Added '{data}' after '{target_data}'")
        
        # Increment size
        self.size += 1

    def insert_before_node(self, data, target_data):
        # Check for empty list
        if self.head is None:
            print(" -> Error: list empty")
            return
        
        # Initialize Variables
        target_node = self.head
        found = False

        # Search for Target Node
        while True:
            if target_node.data == target_data:
                found = True
                break

            target_node = target_node.next

            # Stop search when we loop back to head
            if target_node == self.head:
                break
        
        # Handle Search Result
        if not found:
            print(" -> Error: target data not found")
            return
        
        # Check Edge Case: Inserting before the head
        if target_node == self.head:
            # Re-use insert_at_start logic
            self.insert_at_start(data)
            # The insert_at_start method already handles the printing and size increment
            return
        
        # Insert in the middle
        new_node = Node(data)
        node_before_target = target_node.prev

        # Link new node
        new_node.prev = node_before_target
        new_node.next = target_node

        # Link neighbors
        node_before_target.next = new_node
        target_node.prev = new_node
        
        print(f" -> Added '{data}' before '{target_data}'")
        
        # Increment size
        self.size += 1

    def traverse_forward(self):
        if self.head is None:
            print(" -> Error: You are traversing an Empty List.")
            return
        
        current = self.head
        values = []
        start_node = self.head

        while(current):
            values.append(current.data)
            current = current.next
            if current == start_node:
                break

        print(f"{values} <-->")

    def traverse_backward(self):
        if self.head is None:
            print(" -> Error: You are traversing an Empty List.")
            return
        
        current = self.tail
        values = []
        start_node = self.tail

        while(current):
            values.append(current.data)
            current = current.prev
            if current == start_node:
                break

        print(f"{values} <-->")

if __name__ == "__main__":
    cll = CircularLinkedList()
    print("Daniel caesar: The Playlist")

    cll.insert_at_start("Get you")
    cll.insert_at_start("Always")
    cll.insert_at_start("Frozen")

    # The following target songs did not exist in the previous run, leading to errors.
    # To demonstrate insertion, I'll use existing songs as targets.
    print("\n--- Testing Relative Insertion (Using existing songs) ---")
    cll.insert_after_node("Ivy", "Always") 
    cll.insert_before_node("Time", "Get you")
    
    cll.insert_at_end("Light")
    cll.insert_at_end("Hit my phone")
    cll.insert_at_end("Useless")

    print("\n=== Final Playlist ===")
    cll.traverse_forward()

    cll.show_current_track() # Should be Useless (last inserted at end)

    cll.next_track()
    cll.show_current_track() # Should be Frozen (next track)
    
    cll.prev_track()
    cll.show_current_track() # Should be Useless (prev track)