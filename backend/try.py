from dataclasses import dataclass

@dataclass
class tryData:
    id: int
    title: str
    details: str

dataTest = [
    tryData(
        id=1, title="Title 1", details="Detail 1"
    ),
    tryData(
        id=2, title="Title 2", details="Detail 2"
    )
]
print(dataTest) # This prints the array of data above

expected_title = ["Title 1", "Title 2"]
expected_id = [1, 2]

for data in dataTest:
    print(data)

for idx, task in enumerate(dataTest):
    assert task.id == expected_id[idx]
    assert task.title == expected_title[idx]