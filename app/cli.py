def register_commands(app):
    @app.cli.command("seed_tags")
    def seed_tags():
        from .models import db, Tag  # ✅ move import here to avoid circular import

        tag_names = ['vegan', 'dessert', 'meal', 'snack', 'breakfast', 'gluten-free']
        for name in tag_names:
            if not Tag.query.filter_by(name=name).first():
                db.session.add(Tag(name=name))
        db.session.commit()
        print("Tags seeded successfully.")