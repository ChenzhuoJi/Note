```mermaid
classDiagram
    class Car {
      +String brand
      +int year
      +void start()
    }
    Car <|-- Sedan
    Car <|-- SUV
```
```plantuml
@startuml
Alice -> Bob: Hello
Bob --> Alice: Hi
@enduml
```