```plantuml
@startuml
class Shape 
Shape <|-- LevelsetShape
LevelsetShape *-- BaseLevelSet 
class SPHRelation {
   {abstract} +updateConfiguration()
}
SPHRelation *-- BaseNeighborBuilder
SPHRelation o-- SPHBody
class BaseNeighborBuilder
BaseNeighborBuilder <|-- AdaptiveNeighborBuilder
class SPHBody{
    +redefineShape()
    +generateParticles()
}
class RealBody{
    +redefineAdaptation()
    +definePhysicalMatter()    
}
class BaseAdaptation{
    +createLevelset() 
    +createCellLinkedList()
    +createParticleGenerator()
    +createNeighborBuilder()    
}
class BaseParticleGenerator
BaseParticleGenerator <|-- SurfaceParticleGenerator
class GeometricParticles {
    +poistions_
    +volumetrics_
}
class SurfaceParticles {
    +thickness_
}
class LinearParticles {
    +radius_
}
GeometricParticles <|-- SurfaceParticles
GeometricParticles <|-- LinearParticles
BaseParticleGenerator <|-- LinearParticleGenerator
BaseParticleGenerator <|-- LatticeParticleGenerator
LatticeParticleGenerator <|-- ThickSurfaceParticleGenerator
SPHBody *-- Shape
SPHBody *-- GeometricParticles
class PhysicalMatter {
    +states_
}
RealBody *-- BaseCellLinkedList
RealBody *-- PhysicalMatter
SPHBody *-- BaseAdaptation
SPHBody <|-- RealBody
SPHBody <|-- ObserverBody
PhysicalMatter *-- MaterialProperty
@enduml

```
