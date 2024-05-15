from interstellar_trash_hunter.model.entry import Entry


class Role(Entry):
    """
    角色
    """

    def __init__(self, name, description, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.face = None
        self.skills = []
        self.level = 1
        self.exp = 0
        self.items = []

    def __repr__(self):
        return f"<Role name={self.name} description={self.description}>"

    def __str__(self):
        return f"{self.name} - {self.description}"
