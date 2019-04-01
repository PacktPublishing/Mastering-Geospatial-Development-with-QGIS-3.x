<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.6.1-Brighton" minimumScale="-4.65661e-10" maximumScale="1e+08" hasScaleBasedVisibilityFlag="0">
  <pipe>
    <rasterrenderer opacity="1" alphaBand="0" classificationMax="111" classificationMinMaxOrigin="CumulativeCutFullExtentEstimated" band="1" classificationMin="0" type="singlebandpseudocolor">
      <rasterTransparency>
        <singleValuePixelList>
          <pixelListEntry min="0" max="0" percentTransparent="100"/>
        </singleValuePixelList>
      </rasterTransparency>
      <rastershader>
        <colorrampshader colorRampType="INTERPOLATED" clip="0">
          <item alpha="255" value="0" label="Not Visible" color="#ffffff"/>
          <item alpha="255" value="1" label="Tower 1" color="#fee180"/>
          <item alpha="255" value="10" label="Tower 2" color="#fdc357"/>
          <item alpha="255" value="11" label="Tower 1 and 2" color="#fd9f45"/>
          <item alpha="255" value="100" label="Tower 3" color="#f97534"/>
          <item alpha="255" value="101" label="Towers 1 and 3" color="#f14624"/>
          <item alpha="255" value="110" label="Towers 2 and 3" color="#da2122"/>
          <item alpha="255" value="111" label="Towers 1, 2 and 3" color="#bd0026"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeGreen="128" colorizeOn="0" colorizeRed="255" colorizeBlue="128" grayscaleMode="0" saturation="0" colorizeStrength="100"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
