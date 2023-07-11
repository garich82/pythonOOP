import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = math.ceil(photos_count/4)
        return cls(pages)

    def add_photo(self, label):
        for i, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                slot_number = len(page)
                page_number = i + 1
                return f"{label} photo added successfully on page {page_number} slot {slot_number}"
        return "No more free slots"

    def display(self):
        result = "-" * 11 + "\n"
        for page in self.photos:
            photos_str = " ".join(f"[]" for _ in page) + "\n"
            result += f"{photos_str}{'-' * 11}\n" if photos_str else "-" * 11 + "\n"
        return result


album = PhotoAlbum(3)
for _ in range(8):
    album.add_photo("asdf")
result = album.display().strip()
print(result)