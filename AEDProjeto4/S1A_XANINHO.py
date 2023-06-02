class ChatNode:
    def __init__(self, chat_id, username):
        self.chat_id = chat_id
        self.username = username
        self.prompts = []
        self.left = None
        self.right = None

class ChatSystem:
    def __init__(self):
        self.root = None

    def new_prompt(self, chat_id, username, prompt):
        node = self.find_node(chat_id)
        if node is None:
            # Create new conversation
            new_node = ChatNode(chat_id, username)
            new_node.prompts.append(prompt)
            self.root = self.insert_node(self.root, new_node)
            print(f"CHAT {chat_id} CRIADO")
        else:
            # Add prompt to existing conversation
            node.prompts.append(prompt)
            print(f"CHAT {chat_id} ATUALIZADO")

    def get_chat(self, chat_id):
        node = self.find_node(chat_id)
        if node is None:
            print(f"CHAT {chat_id} NAO ENCONTRADO")
        else:
            print(node.username)
            for prompt in node.prompts:
                print(prompt)
            print("FIM")

    def delete_chat(self, chat_id):
        #if chat_id == 15031:
        #    print(f"CHAT_ID delete AGORA: {chat_id}")
        self.root = self.remove_node(self.root, chat_id)
        #if chat_id == 15031:
        #    print(f"CHAT_ID delete AGORA: {chat_id}")

    def insert_node(self, root, new_node):
        if root is None:
            return new_node

        if new_node.chat_id < root.chat_id:
            root.left = self.insert_node(root.left, new_node)
        elif new_node.chat_id > root.chat_id:
            root.right = self.insert_node(root.right, new_node)

        return root

    def remove_node1(self, root, chat_id):
        if root is None:
            return None

        if chat_id < root.chat_id:
            root.left = self.remove_node1(root.left, chat_id)
        elif chat_id > root.chat_id:
            root.right = self.remove_node1(root.right, chat_id)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            return root

    def remove_node(self, root, chat_id):

        if root is None:
            print(f"CHAT {chat_id} NAO ENCONTRADO")
            return None

        if chat_id < root.chat_id:
            root.left = self.remove_node(root.left, chat_id)
        elif chat_id > root.chat_id:
            root.right = self.remove_node(root.right, chat_id)
        else:
            if root.left is None:
                temp = root.right
                root = None
                print(f"CHAT {chat_id} APAGADO")
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                print(f"CHAT {chat_id} APAGADO")
                return temp
            temp = self.get_min_node_right(root.right)
            root.chat_id = temp.chat_id
            root.username = temp.username
            root.prompts = temp.prompts
            root.right = self.remove_node(root.right, temp.chat_id)


        return root


    def get_min_node_right(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_node(self, chat_id):
        current = self.root
        while current is not None:
            if chat_id < current.chat_id:
                current = current.left
            elif chat_id > current.chat_id:
                current = current.right
            else:
                return current
        return None

chat_system = ChatSystem()

while True:
    command = input().split()
    if command[0] == "NEW_PROMPT":
        chat_system.new_prompt(int(command[1]), command[2], " ".join(command[3:]))
    elif command[0] == "GET_CHAT":
        chat_system.get_chat(int(command[1]))
    elif command[0] == "DELETE_CHAT":
        chat_system.delete_chat(int(command[1]))
        print(int(command[1]))
    elif command[0]== "FIM":
        break
