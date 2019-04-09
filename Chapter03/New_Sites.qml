<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.4.4-Madeira" simplifyMaxScale="1" minScale="1e+08" hasScaleBasedVisibilityFlag="0" maxScale="0" simplifyDrawingHints="0" simplifyAlgorithm="0" labelsEnabled="0" simplifyDrawingTol="1" simplifyLocal="1" styleCategories="AllStyleCategories" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" forceraster="0" enableorderby="0" type="singleSymbol">
    <symbols>
      <symbol alpha="1" clip_to_extent="1" force_rhr="0" type="marker" name="0">
        <layer locked="0" enabled="1" class="SimpleMarker" pass="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="243,166,178,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="dualview/previewExpressions">
      <value>"fid"</value>
    </property>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory width="15" sizeScale="3x:0,0,0,0,0,0" enabled="0" rotationOffset="270" penColor="#000000" lineSizeScale="3x:0,0,0,0,0,0" backgroundAlpha="255" penWidth="0" scaleDependency="Area" penAlpha="255" minimumSize="0" labelPlacementMethod="XHeight" minScaleDenominator="0" diagramOrientation="Up" lineSizeType="MM" backgroundColor="#ffffff" opacity="1" sizeType="MM" scaleBasedVisibility="0" maxScaleDenominator="1e+08" height="15" barWidth="5">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="0" showAll="1" zIndex="0" linePlacementFlags="18" priority="0" obstacle="0" dist="0">
    <properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="site_name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="reference_number">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="land_release_date">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="proposed_construction_date">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="proposal_type">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="fid" name="" index="0"/>
    <alias field="site_name" name="" index="1"/>
    <alias field="reference_number" name="" index="2"/>
    <alias field="land_release_date" name="" index="3"/>
    <alias field="proposed_construction_date" name="" index="4"/>
    <alias field="proposal_type" name="" index="5"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" field="fid" expression=""/>
    <default applyOnUpdate="0" field="site_name" expression=""/>
    <default applyOnUpdate="0" field="reference_number" expression=""/>
    <default applyOnUpdate="0" field="land_release_date" expression=""/>
    <default applyOnUpdate="0" field="proposed_construction_date" expression=""/>
    <default applyOnUpdate="0" field="proposal_type" expression=""/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" notnull_strength="1" constraints="3" field="fid" unique_strength="1"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" field="site_name" unique_strength="0"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" field="reference_number" unique_strength="0"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" field="land_release_date" unique_strength="0"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" field="proposed_construction_date" unique_strength="0"/>
    <constraint exp_strength="0" notnull_strength="0" constraints="0" field="proposal_type" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="fid"/>
    <constraint exp="" desc="" field="site_name"/>
    <constraint exp="" desc="" field="reference_number"/>
    <constraint exp="" desc="" field="land_release_date"/>
    <constraint exp="" desc="" field="proposed_construction_date"/>
    <constraint exp="" desc="" field="proposal_type"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" type="field" hidden="0" name="fid"/>
      <column width="-1" type="field" hidden="0" name="site_name"/>
      <column width="-1" type="field" hidden="0" name="reference_number"/>
      <column width="-1" type="field" hidden="0" name="land_release_date"/>
      <column width="-1" type="field" hidden="0" name="proposed_construction_date"/>
      <column width="-1" type="field" hidden="0" name="proposal_type"/>
      <column width="-1" type="actions" hidden="1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="fid"/>
    <field editable="1" name="land_release_date"/>
    <field editable="1" name="proposal_type"/>
    <field editable="1" name="proposed_construction_date"/>
    <field editable="1" name="reference_number"/>
    <field editable="1" name="site_name"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="fid"/>
    <field labelOnTop="0" name="land_release_date"/>
    <field labelOnTop="0" name="proposal_type"/>
    <field labelOnTop="0" name="proposed_construction_date"/>
    <field labelOnTop="0" name="reference_number"/>
    <field labelOnTop="0" name="site_name"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>fid</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
