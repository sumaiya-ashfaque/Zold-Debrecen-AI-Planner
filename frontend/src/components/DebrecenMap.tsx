import { CircleMarker, MapContainer, Marker, Popup, Polyline, TileLayer } from "react-leaflet"
import "leaflet/dist/leaflet.css"
import L from "leaflet"

const icon = new L.DivIcon({
  className: "plant-marker",
  html: "<div>🌳</div>",
  iconSize: [30, 30],
  iconAnchor: [15, 15],
})

const careIcon = new L.DivIcon({
  className: "care-marker",
  html: "<div>💧</div>",
  iconSize: [30, 30],
  iconAnchor: [15, 15],
})

export default function DebrecenMap({ plan, mode }: { plan: any; mode: string }) {
  const routeLines = (plan?.routes || []).map((route: any) =>
    route.schedule.map((task: any) => [task.coordinate[1], task.coordinate[0]])
  )

  return (
    <MapContainer center={[47.532, 21.627]} zoom={13} className="map">
      <TileLayer
        attribution='&copy; OpenStreetMap contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {(mode === "plant" || mode === "overview") &&
        (plan?.planting_candidates || []).map((feature: any) => {
          const [lon, lat] = feature.geometry.coordinates
          const p = feature.properties
          return (
            <Marker key={p.id} position={[lat, lon]} icon={icon}>
              <Popup>
                <strong>{p.id} · {p.area}</strong><br />
                Opportunity score: {p.opportunity_score}<br />
                Suggested trees: {p.recommended_trees}<br />
                Status: {p.status}
              </Popup>
            </Marker>
          )
        })}

      {(mode === "protect" || mode === "overview") &&
        (plan?.care_priorities || []).map((feature: any) => {
          const [lon, lat] = feature.geometry.coordinates
          const p = feature.properties
          return (
            <Marker key={p.id} position={[lat, lon]} icon={careIcon}>
              <Popup>
                <strong>{p.id} · {p.area}</strong><br />
                {p.recommended_action}<br />
                Care score: {p.care_score}<br />
                Planned water: {p.planned_water_liters} L
              </Popup>
            </Marker>
          )
        })}

      {(mode === "execute" || mode === "overview") &&
        routeLines.map((line: any, i: number) => (
          <Polyline key={i} positions={line} pathOptions={{ weight: 5 }} />
        ))}

      <CircleMarker center={[47.52055, 21.62825]} radius={8}>
        <Popup>Demo operations depot near Debrecen Railway Station</Popup>
      </CircleMarker>
    </MapContainer>
  )
}
