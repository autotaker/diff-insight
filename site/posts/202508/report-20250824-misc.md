---
date: '2025-08-24'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d96708b...MicrosoftDocs:37d9399
summary: このコードの変更では、3つのドキュメントが更新され、エンティティメタデータや固有表現に関する記述の明確化とAPIパラメータの名称変更が行われました。これにより、ドキュメントはより理解しやすくなり、一貫性も向上しました。特に重大な破壊的変更はありませんが、APIパラメータの名称変更に伴い小規模な調整が必要です。更新の目的は、Azure
  Language Serviceの利用者が直面する課題の解決であり、開発者にとってのメタデータの理解やエンティティの識別が容易になることを目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:d96708b...MicrosoftDocs:37d9399){target="_blank"}

# Highlights
このコードの変更では、`entity-metadata.md`, `named-entity-categories.md`, および `how-to-call.md` の3つのドキュメントが更新されました。主な新機能には、エンティティメタデータの詳細な記述や固有表現の一覧の明確化が含まれ、パラメータ名称の改称によるAPIの一貫性向上が見られます。これにより、ドキュメントはユーザーにとってより理解しやすく改善されています。

## New features
- エンティティメタデータの利用方法の明確化。
- 固有表現カテゴリと型の再編成。
- API パラメータの命名変更で一貫性を向上。

## Breaking changes
今回の変更には特に重大な破壊的変更は含まれていませんが、APIのパラメータ名称変更により、既存の実装においては小規模な調整が必要となります。

## Other updates
- セクションの構造整理と表形式での情報追加。
- API バージョン情報の更新と不必要な項目の削除。

# Insights
このドキュメントの更新は、ユーザーがAzure Language Serviceを利用する際に直面する可能性のある課題を解消するために行われました。`entity-metadata.md` ではエンティティメタデータについて具体的で標準化された情報を提供することで、開発者がどのようにメタデータを活用し、サービスをナビゲートするかを明確にしています。

また、`named-entity-categories.md` の更新では、固有表現の認識プロセスやカテゴリとタイプについての情報を再編し、重要な分類を示しました。これにより、開発者はNERを利用する上でのエンティティの正確な識別についてより深い理解を得ることができます。

さらに、`how-to-call.md` でのパラメータ名称の変更は、一貫性をもたらし、プログラムの可読性とメンテナンス性を向上させます。特に大量のAPI呼び出しを行うエンタープライズユーザーにとっては、有用な更新といえます。これにより、サービス利用者がよりスムーズにAzure Language Serviceを統合し、最大限に活用できる環境が整えられました。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [entity-metadata.md](#item-bdb0f6) | minor update | エンティティメタデータ更新 | modified | 367 | 206 | 573 | 
| [named-entity-categories.md](#item-a4a7f1) | minor update | 固有表現カテゴリの再構成 | modified | 281 | 842 | 1123 | 
| [how-to-call.md](#item-c5709f) | minor update | エンティティ検出リストのパラメータ名称変更 | modified | 7 | 7 | 14 | 


# Modified Contents
## articles/ai-services/language-service/named-entity-recognition/concepts/entity-metadata.md{#item-bdb0f6}

<details>
<summary>Diff</summary>
````diff
@@ -1,85 +1,119 @@
 ---
-title: Entity Metadata provided by Named Entity Recognition
+title: Entity Metadata provided by Named Entity Recognition (NER)
 titleSuffix: Azure AI services
-description: Learn about entity metadata in the NER feature.
+description: View entity metadata values for named entity recognition (NER) named entities.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 06/21/2025
+ms.date: 08/22/2025
 ms.author: lajanuar
 ms.custom: language-service-ner
 ---
 
 # Entity Metadata
 
-The Entity Metadata object captures optional additional information about detected entities, providing resolutions specifically for numeric and temporal entities. This attribute is populated only when there's supplementary data available, enhancing the comprehensiveness of the detected entities. The Metadata component encompasses resolutions designed for both numeric and temporal entities. It's important to handle cases where the Metadata attribute may be empty or absent, as its presence isn't guaranteed for every entity.
+The entity metadata object stores optional supplementary details about detected entities, specifically providing standardized resolutions for numeric and temporal data. 
 
-Currently, metadata components handle resolutions to a standard format for an entity. Entities can be expressed in various forms and resolutions provide standard predictable formats for common quantifiable types. For example, "eighty" and "80" should both resolve to the integer `80`.
+This attribute is only populated when extra information is available and may be empty or missing for some entities. 
+
+Metadata resolutions convert various entity forms into consistent formats—for example, both "eighty" and "80" resolve to the integer 80. These NER resolutions enable downstream actions, such as extracting date and time entities for integration with a meeting scheduling system.
 
-You can use NER resolutions to implement actions or retrieve further information. For example, your service can extract datetime entities to extract dates and times that are provided to a meeting scheduling system. 
 
 > [!NOTE]
->  Entity Metadata are only supported starting from **_api-version=2023-04-15-preview_**. For older API versions, you may check the [Entity Resolutions article](./entity-resolutions.md).
+>  Support for Entity Metadata is available with API `2023-04-15-preview` and later versions. For older API versions, see [Entity Resolutions](./entity-resolutions.md).
+
+## Entities with metadata attributes
 
-This article documents the resolution objects returned for each entity category or subcategory under the metadata object.
+|Entities|Entities|Entities|Entities|Entities|Entities|
+|:---:|:---:|:---:|:---:|:---:|:---:|
+|[Age](#age)|[Area](#area)|[Currency](#currency)|[Date](#date)|[Datetime](#datetime)|[Information](#information)|
+|[Length](#length)|[Number](#number)|[NumericRange](#numericrange)|[Ordinal](#ordinal)|[Set](#set)|[Speed](#speed)|
+|[Temperature](#temperature)|[Time](#time)|[Volume](#volume)|[Weight](#weight)|||
 
-## Numeric Entities
 
 ### Age
 
-Examples: "10 years old", "23 months old", "sixty Y.O."
+|Metadata|Type|Description|
+|---|---|---|
+|**unit**|string|Unit of measurement for age.|
+|**value**|number|Numeric value for age.|
 
 ```json
 "metadata": {
-                "metadataKind": "AgeMetadata",
                 "unit": "Year",
                 "value": 10
             }
-```              
+```
+
+**Possible values for *unit***:
+
+* Day
+* Month
+* Week
+* Year
+* Unspecified
+
+
+### Area
 
-Possible values for "unit":
-- Year
-- Month
-- Week
-- Day
+|Metadata|Type|Description|
+|---|---|---|
+|**unit**|string|Unit of measurement for area.|
+|**value**|number|Numeric value for area.|
+
+
+```JSON
+"metadata": {
+                "unit": "Acre",
+                "value": 30
+            }
+```
 
+**Possible values for *unit***:
+
+* Acre
+* SquareCentimeter
+* SquareDecameter
+* SquareDecimeter
+* SquareFoot
+* SquareHectometer
+* SquareInch
+* SquareKilometer
+* SquareMeter
+* SquareMile
+* SquareMillimeter
+* SquareYard
+* Unspecified
 
 ### Currency
 
-Examples: "30 Egyptian pounds", "77 USD"
+|Metadata|Type|Description|
+|---|---|---|
+|**unit**|string|Name of currency.|
+|**value**|number|Numeric value for currency.|
+|**ISO4217**|string|The ISO 4217 three-letter currency code uses the first two letters from the country's ISO 3166 code, and, when possible, the third letter is the first letter of the currency name.|
 
 ```json
 "metadata": {
                 "unit": "Egyptian pound",
-                "ISO4217": "EGP",
-                "value": 30
+                "value": 30,
+                "ISO4217": "EGP"
             }
 ```
 
-Possible values for "unit" and "ISO4217":
+**Possible values for *ISO4217***:
 - [ISO 4217 reference](https://docs.1010data.com/1010dataReferenceManual/DataTypesAndFormats/currencyUnitCodes.html).
 
-## Datetime/Temporal entities
 
-Datetime includes several different subtypes that return different response objects.
 
 ### Date
 
-Specific days.
+|Metadata|Type|Description|
+|---|---|---|
+|**timex**|string|The ISO 8601 formatted date: `YYYY-MM-DD` (year, month, day). |
+|**value**|string|The actual denoted date.|
 
-Examples: "January 1 1995", "12 april", "7th of October 2022", "tomorrow"
-
-```json
-"metadata": {
-                "dateValues": [
-                    {
-                        "timex": "1995-01-01",
-                        "value": "1995-01-01"
-                    }
-                ]
-            }
-```
 
 Whenever an ambiguous date is provided, you're offered different options for your resolution. For example, "12 April" could refer to any year. Resolution provides this year and the next as options. The `timex` value `XXXX` indicates no year was specified in the query.
 
@@ -98,7 +132,7 @@ Whenever an ambiguous date is provided, you're offered different options for you
             }
 ```
 
-Ambiguity can occur even for a given day of the week. For example, saying "Monday" could refer to last Monday or this Monday. Once again the `timex` value indicates no year or month was specified, and uses a day of the week identifier (W) to indicate the first day of the week. 
+Ambiguity can occur even for a given day of the week. For example, saying "Monday" could refer to last Monday or this Monday. Once again the `timex` value indicates no year or month was specified, and uses a day of the week identifier (W) to indicate the first day of the week.
 
 ```json
 "metadata" :{
@@ -115,233 +149,360 @@ Ambiguity can occur even for a given day of the week. For example, saying "Monda
             }
 ```
 
+### Datetime
 
-### Time
-
-Specific times.
+|Metadata|Type|Description|
+|---|---|---|
+|timex|string|The ISO 8601 formatted date and time:<br>`YYYY-MM-DDTHH:MM:SS`(year, month, day, hour, minutes, seconds, milliseconds) with a `T` separator. |
+|value|string|The actual denoted date and time.|
 
-Examples: "9:39:33 AM", "seven AM", "20:03"
+Similar to dates, you can have ambiguous datetime entities. Resolution provides this year and the next as options. The `timex` value **XXXX** indicates no year was specified.
 
 ```json
 "metadata": {
-                "timex": "T09:39:33",
-                "value": "09:39:33"
-            }
+                 "dateValues": [
+                       {
+                           "timex": "XXXX-05-03T12",
+                           "value": "2022-05-03 12:00:00"
+                       },
+                       {
+                           "timex": "XXXX-05-03T12",
+                           "value": "2023-05-03 12:00:00"
+                       }
+                  ]
+              }
 ```
 
-### Datetime
-
-Specific date and time combinations.
+### Information
 
-Examples: "6 PM tomorrow", "8 PM on January 3rd", "Nov 1 19:30"
+|Metadata|Type|Description|
+|---|---|---|
+|**unit**|string|Unit of measurement for information (data).|
+|**value**|number|Numeric value for information.|
 
 ```json
+
 "metadata": {
-                "timex": "2022-10-07T18",
-                "value": "2022-10-07 18:00:00"
+                "unit": "Kilobit",
+                "value": 30
             }
+
 ```
 
-Similar to dates, you can have ambiguous datetime entities. For example, "May 3rd noon" could refer to any year. Resolution provides this year and the next as options. The `timex` value **XXXX** indicates no year was specified. 
+**Possible values for *unit***:
+
+* Bit
+* Byte
+* Gigabit
+* Gigabyte
+* Kilobit
+* Kilobyte
+* Megabit
+* Megabyte
+* Petabit
+* Petabyte
+* Terabit
+* Terabyte
+* Unspecified
+
+### Length
+
+|Metadata|Type|Description|
+|---|---|---|
+|**unit**|string|Unit of measurement for length|
+|**value**|number|Numeric value.|
 
 ```json
+
 "metadata": {
-                 "dateValues": [ 
-                       {
-                           "timex": "XXXX-05-03T12",
-                           "value": "2022-05-03 12:00:00"
-                       },
-                       {
-                           "timex": "XXXX-05-03T12",
-                           "value": "2023-05-03 12:00:00"
-                       }
-                  ]
-              }
+                "unit": "Kilobit",
+                "value": 30
+            }
+
 ```
+**Possible values for *unit***:
+
+* Centimeter
+* Decameter
+* Decimeter
+* Foot
+* Hectometer
+* Inch
+* Kilometer
+* LightYear
+* Meter
+* Micrometer
+* Mile
+* Millimeter
+* Nanometer
+* Picometer
+* Point
+* Yard
+* Unspecified
+
+### Number
+
+|Metadata|Type|Description|
+|---|---|---|
+|**numberKind**|string|Number type.|
+|**value**|number|Numeric value for number.|
+
+```json
+
+"metadata": {
+                "numberKind": "Integer",
+                "value": 30
+            }
+
+```
+
+**Possible values for *numberKind***:
 
-### Datetime ranges
+* Decimal
+* Fraction
+* Integer
+* Percent
+* Power
+* Unspecified
 
-A datetime range is a period with a beginning and end date, time, or datetime.
+### NumericRange
 
-Examples: "from january 3rd 6 AM to april 25th 8 PM 2022", "between Monday to Thursday", "June", "the weekend"
+|Metadata|Type|Description|
+|---|---|---|
+|**rangeKind**|string|A supported numeric range.|
+|**minimum**|number|The beginning value of  the interval.|
+|**maximum**|number|The ending value of the interval.|
 
-The "duration" parameter indicates the time passed in seconds (S), minutes (M), hours (H), or days (D). This parameter is only returned when an explicit start and end datetime are in the query. "Next week" would only return with "begin" and "end" parameters for the week.
+```json
+
+"metadata": {
+                "rangeKind": "length",
+                "minimum": 30,
+                "maximum": 100
+            }
+
+```
+**Possible values for *rangeKind***:
+
+* Age
+* Area
+* Currency
+* Information
+* Length
+* Number
+* Speed
+* Temperature
+* Volume
+* Weight
+
+### Ordinal
+
+|Metadata|Type|Description|
+|---|---|---|
+|**offset**|string|The offset with respect to the reference (for example, offset = -1 indicates the second to last)|
+|**relativeTo**|The reference point that the ordinal number denotes.|
+|**value**|number|Numeric value for ordinal position.|
 
 ```json
+
 "metadata": {
-                "duration": "PT2702H",
-                "begin": "2022-01-03 06:00:00",
-                "end": "2022-04-25 20:00:00"
+                "offset": -1,
+                "relativeTo":"Current",
+                "value": "first"
             }
+
 ```
 
+**Possible values for *relativeTo***:
+
+* Current
+* End
+* Start
+
 ### Set
 
-A set is a recurring datetime period. Sets don't resolve to exact values, as they don't indicate an exact datetime. 
+A recurring datetime period (example: "every Monday at 6:00 PM.")
 
-Examples: "every Monday at 6 PM", "every Thursday", "every weekend"
+|Metadata|Type|Description|
+|---|---|---|
+|**timex**|string|The ISO 8601 formatted date and time:<br>`YYYY-MM-DDTHH:MM:SS`(year, month, day, hour, minutes, seconds, milliseconds) with a `T` separator. |
+|**value**|string|Sets don't resolve to exact values, as they don't indicate an exact datetime.|
 
-For "every Monday at 6 PM", the `timex` value indicates no specified year with the starting **XXXX**, then every Monday through **WXX-1** to determine first day of every week, and finally **T18** to indicate 6 PM. 
 
 ```json
+
 "metadata": {
                 "timex": "XXXX-WXX-1T18",
                 "value": "not resolved"
             }
+
 ```
 
-## Dimensions
+**Possible values for *type***:
+
+* begin
+* end
+* duration
+* modifier (example: `before`, `after`)
+* timex
 
-Examples: "24 km/hr", "44 square meters", "sixty six kilobytes"
+
+### Speed
+
+|Metadata|Type|Description|
+|---|---|---|
+|**unit**|string|Unit of measurement for speed.|
+|**value**|number|Numeric value for speed.|
 
 ```json
+
 "metadata": {
-                "unit": "KilometersPerHour",
-                "value": 24
+                "unit": "Knots",
+                "value": 50
             }
+
 ```
 
-Possible values for the "unit" field values:
-
-- **For Measurements**:
-  - SquareKilometer
-  - SquareHectometer
-  - SquareDecameter
-  - SquareMeter
-  - SquareDecimeter
-  - SquareCentimeter
-  - SquareMillimeter
-  - SquareInch
-  - SquareFoot
-  - SquareMile
-  - SquareYard
-  - Acre
-
-- **For Information**:
-  - Bit
-  - Kilobit
-  - Megabit
-  - Gigabit
-  - Terabit
-  - Petabit
-  - Byte
-  - Kilobyte
-  - Megabyte
-  - Gigabyte
-  - Terabyte
-  - Petabyte
-  
-- **For Length, width, height**:
-  - Kilometer
-  - Hectometer
-  - Decameter
-  - Meter
-  - Decimeter
-  - Centimeter
-  - Millimeter
-  - Micrometer
-  - Nanometer
-  - Picometer
-  - Mile
-  - Yard
-  - Inch
-  - Foot
-  - Light year
-  - Pt
-
-- **For Speed**:
-  - MetersPerSecond
-  - KilometersPerHour
-  - KilometersPerMinute
-  - KilometersPerSecond
-  - MilesPerHour
-  - Knot
-  - FootPerSecond
-  - FootPerMinute
-  - YardsPerMinute
-  - YardsPerSecond
-  - MetersPerMillisecond
-  - CentimetersPerMillisecond
-  - KilometersPerMillisecond
-
-- **For Volume**:
-  - CubicMeter
-  - CubicCentimeter
-  - CubicMillimiter
-  - Hectoliter
-  - Decaliter
-  - Liter
-  - Deciliter
-  - Centiliter
-  - Milliliter
-  - CubicYard
-  - CubicInch
-  - CubicFoot
-  - CubicMile
-  - FluidOunce
-  - Teaspoon
-  - Tablespoon
-  - Pint
-  - Quart
-  - Cup
-  - Gill
-  - Pinch
-  - FluidDram
-  - Barrel
-  - Minim
-  - Cord
-  - Peck
-  - Bushel
-  - Hogshead
-
-- **For Weight**:
-  - Kilogram
-  - Gram
-  - Milligram
-  - Microgram
-  - Gallon
-  - MetricTon
-  - Ton
-  - Pound
-  - Ounce
-  - Grain
-  - Pennyweight
-  - LongTonBritish
-  - ShortTonUS
-  - ShortHundredweightUS
-  - Stone
-  - Dram
-
-
-## Ordinal
-
-Examples: "3rd", "first", "last"
+**Possible values for *unit***:
+
+* CentimetersPerMillisecond
+* FeetPerMinute
+* FeetPerSecond
+* KilometersPerHour
+* KilometersPerMillisecond
+* KilometersPerMinute
+* KilometersPerSecond
+* Knots
+* MetersPerMillisecond
+* MetersPerSecond
+* MilesPerHour
+* YardsPerMinute
+* YardsPerSecond
+* Unspecified
+
+### Temperature
+
+|Metadata|Type|Description|
+|---|---|---|
+|**unit**|string|Unit of measurement for temperature.|
+|**value**|number|Numeric value.|
 
 ```json
+
 "metadata": {
-                "offset": "3",
-                "relativeTo": "Start",
-                "value": "3"
+                "unit" "Kelvin",
+                "value": 310
             }
+
 ```
+**Possible values for *unit***:
+
+* Celsius
+* Fahrenheit
+* Kelvin
+* Rankine
+* Unspecified
+
+
+
+### Time
+
+|Metadata|Type|Description|
+|---|---|---|
+|**timex**|string|The ISO 8601 formatted date time:<br>`[hh]:[mm]:[ss]`(hour, minutes, seconds).|
+|**value**|number|Numeric value.|
+
+```json
 
-Possible values for "relativeTo":
-- Start
-- End
+"metadata": {
+                "timex":"T14:30:15",
+                "value": "14:30:15"
+            }
 
-## Temperature
+```
 
-Examples: "88 deg fahrenheit", "twenty three degrees celsius"
+### Volume
+
+|Metadata|Type|Description|
+|---|---|---|
+|**unit**|string|Unit of measurement for volume.|
+|**value**|number|Numeric value for volume.|
 
 ```json
+
 "metadata": {
-                "unit": "Fahrenheit",
-                "value": 88
+                "unit": "Quart",
+                "value": 4
             }
+
 ```
+**Possible values for *unit***:
+
+* Barrel
+* Bushel
+* Centiliter
+* Cord
+* CubicCentimeter
+* CubicFoot
+* CubicInch
+* CubicMeter
+* CubicMile
+* CubicMillimeter
+* CubicYard
+* Cup
+* Decaliter
+* FluidDram
+* FluidOunce
+* Gill
+* Hectoliter
+* Hogshead
+* Liter
+* Milliliter
+* Minim
+* Peck
+* Pinch
+* Pint
+* Quart
+* Tablespoon
+* Teaspoon
+* Unspecified
+
+### Weight
+
+|Metadata|Type|Description|
+|---|---|---|
+|**unit**|string|Unit of measurement for weight.|
+|**value**|number|Numeric value for weight.|
 
-Possible values for "unit":
-- Celsius
-- Fahrenheit
-- Kelvin
-- Rankine
+```json
+
+"metadata": {
+                "unit": "Ounce",
+                "value": 16
+            }
+
+```
+**Possible values for *unit***:
+
+* Dram
+* Gallon
+* Grain
+* Gram
+* Kilogram
+* LongTonBritish
+* MetricTon
+* Milligram
+* Ounce
+* PennyWeight
+* Pound
+* ShortHundredWeightUS
+* ShortTonUS
+* Stone
+* Ton
+* Unspecified
+
+
+## Next steps
+
+
+Learn [how to use NER](../how-to-call.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティメタデータ更新"
}
```

### Explanation
このコードの差分は、`entity-metadata.md` におけるエンティティメタデータに関する文書の内容を改善するための変更を示しています。具体的には、以下のような内容が含まれています。

- タイトルが「Named Entity Recognition (NER)」を含む形に変更され、より具体的になりました。
- 説明文も更新され、エンティティメタデータの利用方法がより明確に記述されています。
- エンティティメタデータオブジェクトの説明が簡潔化され、標準化された解決策の提供について言及されています。
- セクションの構造が整理され、表形式での情報提供が追加され、多くのメタデータ（年齢、地域、通貨、日付など）についての詳細が記載されています。
- メタデータの可能な値や型に関する説明が増え、ユーザーが利用しやすい情報が強化されています。
- API バージョンに関する注意書きが更新され、サポートされるバージョンが明示されています。

全体的に、ドキュメントは現行の利用方法および技術的詳細に対してより透明性を提供する形で進化しており、ユーザーがエンティティメタデータとその使用方法を理解するのに役立つよう改良されています。

## articles/ai-services/language-service/named-entity-recognition/concepts/named-entity-categories.md{#item-a4a7f1}

<details>
<summary>Diff</summary>
````diff
@@ -6,1016 +6,455 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 05/23/2025
+ms.date: 08/06/2025
 ms.author: lajanuar
 ms.custom: language-service-ner
 ---
 
-# Supported Named Entity Recognition (NER) entity categories and entity types
+# Named entity categories and types
 
-Use this article to find the entity categories that can be returned by [Named Entity Recognition (NER)](../how-to-call.md). NER runs a predictive model to identify and categorize named entities from an input document. 
+Named Entity Recognition (NER) is a computational linguistic process within natural language processing (NLP) that uses predictive models to detect and identify entities within unstructured text. After entities are detected, each entity receives a semantic label and is organized into predefined categories and types:
 
-> [!NOTE]
-> * Starting from API version 2023-04-15-preview, the category and subcategory fields are replaced with entity types and tags to introduce better flexibility. 
-
-# [Generally Available API](#tab/ga-api)
- 
-## Type: Person
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Person
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Names of people.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `ar`, `cs`, `da`, `nl`, `en`, `fi`, `fr`, `de`, `he`, <br> `hu`, `it`, `ja`, `ko`, `no`, `pl`, `pt-br`, `pt`-`pt`, `ru`, `es`, `sv`, `tr`   
-      
-   :::column-end:::
-:::row-end:::
-
-## Type: PersonType
-
-This type contains the following entity:
-
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        PersonType
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Job types or roles held by a person
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`  
-      
-   :::column-end:::
-:::row-end:::
-
-## Type: Location
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Location
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Natural and human-made landmarks, structures, geographical features, and geopolitical entities.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `ar`, `cs`, `da`, `nl`, `en`, `fi`, `fr`, `de`, `he`, `hu`, `it`, `ja`, `ko`, `no`, `pl`, `pt-br`, `pt-pt`, `ru`, `es`, `sv`, `tr`   
-      
-   :::column-end:::
-:::row-end:::
-
-#### Subtype
-
-The entity in this type can have the following subtypes.
-
-:::row:::
-    :::column span="":::
-        **Entity subtype**
-
-        Geopolitical Entity (GPE)
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Cities, countries/regions, states.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-
-        Structural
-
-    :::column-end:::
-    :::column span="2":::
-
-        Manmade structures. 
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-
-        Geographical
-
-    :::column-end:::
-    :::column span="2":::
-
-        Geographic and natural features such as rivers, oceans, and deserts.
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`   
-      
-   :::column-end:::
-:::row-end:::
-
-## Type: Organization
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Organization
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Companies, political groups, musical bands, sport clubs, government bodies, and public organizations. Nationalities and religions are not included in this entity type.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `ar`, `cs`, `da`, `nl`, `en`, `fi`, `fr`, `de`, `he`, `hu`, `it`, `ja`, `ko`, `no`, `pl`, `pt-br`, `pt-pt`, `ru`, `es`, `sv`, `tr`   
-      
-   :::column-end:::
-:::row-end:::
-
-#### Subtype
-
-The entity in this type can have the following subtype.
-
-:::row:::
-    :::column span="":::
-        **Entity subtype**
-
-        Medical
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Medical companies and groups.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `en`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+* **Entity Categories** refer to main classifications of named entities such as Location, Organization, Date, or Quantity.
 
-        Stock exchange
+* **Entity Types** provide more detailed distinctions within the broader categories, allowing for more granularity and flexibility.
 
-    :::column-end:::
-    :::column span="2":::
+This article provides a list of entity categories identified and returned by the Named Entity Recognition (NER) process.## Language Support
 
-        Stock exchange groups. 
-      
-    :::column-end:::
-    :::column span="2":::
 
-      `en`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+The [NER language support](../language-support.md) page lists all languages available for the named entities in this article. Any exceptions are noted for specific named entities.
 
-        Sports
+Supported API versions:
 
-    :::column-end:::
-    :::column span="2":::
+* [**Preview: 2025-05-15-preview**](/rest/api/language/text-analysis-runtime/analyze-text?view=rest-language-2025-05-15-preview&preserve-view=true&tabs=HTTP#entitycategory)
+* [**Stable: Generally Available (GA)**](/rest/api/language/text-analysis-runtime/analyze-text?view=rest-language-2024-11-01&preserve-view=truetabs=HTTP#entitycategory)
 
-        Sports-related organizations.
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`   
-      
-   :::column-end:::
-:::row-end:::
-
-## Type: Event
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Event
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Historical, social, and naturally occurring events.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt` and `pt-br`  
-      
-   :::column-end:::
-:::row-end:::
-
-#### Subtypes
-
-The entity in this type can have the following subtype.
-
-:::row:::
-    :::column span="":::
-        **Entity subtype**
-
-        Cultural
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Cultural events and holidays.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `en`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-
-        Natural
-
-    :::column-end:::
-    :::column span="2":::
-
-        Naturally occurring events.
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-
-        Sports
-
-    :::column-end:::
-    :::column span="2":::
-
-        Sporting events.
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`   
-      
-   :::column-end:::
-:::row-end:::
-
-## Type: Product
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Product
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Physical objects of various types.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`  
-      
-   :::column-end:::
-:::row-end:::
-
-
-#### Subtype
-
-The entity in this type can have the following subtype.
-
-:::row:::
-    :::column span="":::
-        **Entity subtype**
-
-        Computing products
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Computing products.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `en`   
-      
-   :::column-end:::
-:::row-end:::
-
-## Type: Skill
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Skill
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        A capability, skill, or expertise.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `en` , `es`, `fr`, `de`, `it`, `pt-pt`, `pt-br` 
-      
-   :::column-end:::
-:::row-end:::
-
-## Type: Address
-
-This type contains the following entity:
-
-:::row:::
-    :::column span="":::
-        **Entity**
+> [!NOTE]
+> Beginning with the GA API (released 2024-11-01), the **Subcategory** field is no longer supported. All entity classifications now use the **type** field.
+
+## NER named entity types
+
+|Entities|Entities|Entities|Entities|Entities|Entities|
+|:---:|:---:|:---:|:---:|:---:|:---:|
+|[Address](#type-address)|[Age](#type-age)|[Airport](#type-airport)|[Area](#type-area)|[City](#type-city)|[ComputingProduct](#type-computingproduct)|
+|[Continent](#type-continent)|[CountryRegion](#type-countryregion)|[CulturalEvent](#type-culturalevent)|[Currency](#type-currency)|[Date](#type-date)|[DateRange](#type-daterange)|
+|[DateTime](#type-datetime)|[DateTimeRange](#type-datetimerange)|[Dimension](#type-dimension)|[Duration](#type-duration)|[Email](#type-email)|[Event](#type-event)|
+|[Geological](#type-geographical)|[GPE](#type-gpe)|[Height](#type-height)|[Information](#type-information)|[IpAddress](#type-ipaddress)|[Length](#type-length)|
+|[Location](#type-location)|[NaturalEvent](#type-naturalevent)|[Number](#type-number)|[NumberRange](#type-numberrange)|[Ordinal](#type-ordinal)|[Organization](#type-organization)|
+|[OrganizationMedical](#type-organizationmedical)|[OrganizationSports](#type-organizationsports)|[OrganizationStockExchange](#type-organizationstockexchange)|[Percentage](#type-percentage)|[Person](#type-person)|[PersonType](#type-persontype)|
+|[PhoneNumber](#type-phonenumber)|[Product](#type-product)|[SetTemporal](#type-settemporal)|[Skill](#type-skill)|[Speed](#type-speed)|[SportsEvent](#type-sportsevent)|
+|[State](#type-state)|[Structural](#type-structural)|[Temporal](#type-temporal)|[Temperature](#type-temperature)|[Time](#type-time)|[TimeRange](#type-timerange)|
+|[URL](#type-url)|[Volume](#type-volume)|[Weight](#type-weight)||
 
-        Address
+### Type: Address
+##### Category: Location
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Entity|Tags|Detail|
+|---|---|---|
+|**Address**|Address|A distinct identifier assigned to a physical or geographic location, utilized for navigation, delivery services, and formal administrative purposes.|
 
-        Full mailing address.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
+### Type: Age
+##### Category: Quantity
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
-      
-   :::column-end:::
-:::row-end:::
 
-## Type: PhoneNumber
+|Entity|Tags|Detail|Metadata|
+|---|---|---|---|
+|**Age**|Numeric, Quantity, Age|A quantitative measure representing the length of time from an individual's birth to a specific reference date.|[Age metadata](entity-metadata.md#age)|
 
-This type contains the following entity:
 
-:::row:::
-    :::column span="":::
-        **Entity**
+### Type: Airport
+##### Category: Airport
 
-        PhoneNumber
+|Entity|Tags|Detail|
+|---|---|---|
+|**Airport**|Airport|A designated location equipped with facilities for the landing, takeoff, and maintenance of aircraft.  |
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Area
+##### Category: Quantity
 
-        Phone numbers (US and EU phone numbers only).
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Area**|Numeric, Quantity, Dimension, Area|The measurement of a surface or region expressed in square units.|[Area metadata](entity-metadata.md#area)|
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt` `pt-br`
-      
-   :::column-end:::
-:::row-end:::
+### Type: City
+##### Category: Location
 
-## Type: Email
+|Entity|Tags|Detail|
+|---|---|---|
+|**City**|Location,GPE,City|A settlement characterized by a dense population and infrastructure. |
 
-This type contains the following entity:
+### Type: ComputingProduct
+##### Category: Product
 
-:::row:::
-    :::column span="":::
-        **Entity**
+|Entity|Tags|Detail|
+|---|---|---|
+|**ComputingProduct**|Product, ComputingProduct|A hardware or software item designed for computational tasks or digital processing.|
 
-        Email
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Continent
+##### Category: Location
 
-        Email addresses.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
-      
-   :::column-end:::
-:::row-end:::
+|Entity|Tags|Detail|
+|---|---|---|
+|**Continent**|Location,GPE,Continent|A vast, continuous landmass on the Earth's surface. | 
 
-## Type: URL
 
-This type contains the following entity:
+### Type: CountryRegion
+##### Category: Location
 
-:::row:::
-    :::column span="":::
-        **Entity**
+|Entity|Tags|Detail|
+|---|---|---|
+|**CountryRegion**|Location,GPE,CountryRegion|A distinct territorial entity recognized as a nation or administrative area.|
 
-        URL
+### Type: CulturalEvent
+##### Category: Event
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+|Entity|Tags|Detail|Language support|
+|---|---|---|---|
+|**CulturalEvent**|Event, EventCultural|An organized activity or gathering that reflects or celebrates cultural practices or traditions| `en`|
 
-        URLs to websites. 
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
-      
-   :::column-end:::
-:::row-end:::
+### Type: Currency
+##### Category: Quantity
 
-## Type: IP
 
-This type contains the following entity:
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Currency**|Numeric, Quantity, Currency|A system of money in common use, typically issued by a government and used as a medium of exchange.|[Currency metadata](entity-metadata.md#currency)|
 
-:::row:::
-    :::column span="":::
-        **Entity**
 
-        IP
+### Type: Date
+##### Category: DateTime
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
 
-        network IP addresses. 
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
+|Entity|Tags|Detail|MetaData|
+|---|---|---|
+|**Date**|DateTime, Date|A specific calendar day expressed in terms of day, month, and year.|[Date metadata](entity-metadata.md#date)|
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
-      
-   :::column-end:::
-:::row-end:::
 
-## Type: DateTime
+### Type: DateRange
+##### Category: DateTime
 
-This type contains the following entities:
 
-:::row:::
-    :::column span="":::
-        **Entity**
+|Entity|Tags|Detail|
+|---|---|---|
+|**DateRange**|DateTime, DateRange|A span of time defined by a start and end date.|
 
-        DateTime
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: DateTime
+##### Category: DateTime
 
-        Dates and times of day. 
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
-      
-   :::column-end:::
-:::row-end:::
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**DateTime**|DateTime|A data type encompassing date and time components used in scheduling or logging events.|[DateTime metadata](entity-metadata.md#datetime)|
 
-Entities in this type can have the following subtypes
 
-#### Subtypes
+### Type: DateTimeRange
+##### Category: DateTime
 
-The entity in this type can have the following subtypes.
 
-:::row:::
-    :::column span="":::
-        **Entity subtype**
+|Entity|Tags|Detail|
+|---|---|---|
+|**DateTimeRange**|DateTime, DateTimeRange|A period defined by a starting and ending date and time.|
 
-        Date
 
-    :::column-end:::
-    :::column span="2":::
-        **Details**
+### Type: Dimension
+##### Category: Quantity
 
-        Calender dates.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Entity|Tags|Detail|
+|---|---|---|
+|**Dimension**|Numeric, Quantity, Dimension|The measurable size or extent of an object or area, commonly expressed in terms of length, width, height, or depth.|
 
-        Time
 
-    :::column-end:::
-    :::column span="2":::
+### Type: Duration
+##### Category: DateTime
 
-        Times of day.
-      
-    :::column-end:::
-    :::column span="2":::
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
+|Entity|Tags|Detail|
+|---|---|---|
+|**Duration**|DateTime, Duration|The total time interval during which an event occurs or continues.|
 
-        DateRange
 
-    :::column-end:::
-    :::column span="2":::
+### Type: Email
+##### Category: Email
 
-        Date ranges.
-      
-    :::column-end:::
-    :::column span="2":::
+|Entity|Tags|Detail|
+|---|---|---|
+|**Email**|Email|An electronic message sent and received via digital mail systems.|
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`  
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
 
-        TimeRange
+### Type: Event
+##### Category: Event
 
-    :::column-end:::
-    :::column span="2":::
 
-        Time ranges.
-      
-    :::column-end:::
-    :::column span="2":::
+|Entity|Tags|Detail|
+|---|---|---|
+|**Event**|Event|A specific or noteworthy instance, or activity occurring within a defined context.|
 
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`  
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-
-        Duration
 
-    :::column-end:::
-    :::column span="2":::
+### Type: Geographical
+##### Category: Location
 
-        Durations.
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`  
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-
-        Set
-
-    :::column-end:::
-    :::column span="2":::
-
-        Set, repeated times.
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`  
-      
-   :::column-end:::
-:::row-end:::
-
-## Type: Quantity
-
-This type contains the following entities:
-
-:::row:::
-    :::column span="":::
-        **Entity**
-
-        Quantity
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Numbers and numeric quantities.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `ja`, `ko`, `pt-pt`, `pt-br`
-      
-   :::column-end:::
-:::row-end:::
-
-#### Subtypes
-
-The entity in this type can have the following subtypes.
-
-:::row:::
-    :::column span="":::
-        **Entity subtype**
-
-        Number
-
-    :::column-end:::
-    :::column span="2":::
-        **Details**
-
-        Numbers.
-      
-    :::column-end:::
-    :::column span="2":::
-      **Supported document languages**
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-        Percentage
-
-    :::column-end:::
-    :::column span="2":::
-
-        Percentages
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-        Ordinal numbers
-
-    :::column-end:::
-    :::column span="2":::
-
-        Ordinal numbers.
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-        Age
-
-    :::column-end:::
-    :::column span="2":::
-
-        Ages.
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-        Currency
-
-    :::column-end:::
-    :::column span="2":::
-
-        Currencies
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-        Dimensions
-
-    :::column-end:::
-    :::column span="2":::
-
-        Dimensions and measurements.
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
-      
-   :::column-end:::
-:::row-end:::
-:::row:::
-    :::column span="":::
-        Temperature
-
-    :::column-end:::
-    :::column span="2":::
-
-        Temperatures.
-      
-    :::column-end:::
-    :::column span="2":::
-
-      `en`, `es`, `fr`, `de`, `it`, `zh-hans`, `pt-pt`, `pt-br`   
-      
-   :::column-end:::
-:::row-end:::
-
-# [Preview API](#tab/preview-api)
+|Entity|Tags|Detail|
+|---|---|---|
+|**Geographical**|Location, Geographical|Earth's physical geography and natural features, including landforms like rivers, mountains, and valleys.|
 
-### Type: Address
+### Type: GPE
+##### Category: Location
 
-Specific street-level mentions of locations: house/building numbers, streets, avenues, highways, intersections referenced by name.
+|Entity|Tags|Detail|
+|---|---|---|
+|**GPE**|Location, GPE|Geo political entity (GPE) is a region or area defined by political boundaries or governance. |
 
-### Type: Numeric
 
-Numeric values.
+### Type: Height
+##### Category: Quantity
 
-This entity type could be tagged by the following entity tags:
+|Entity|Tags|Detail|
+|---|---|---|
+|**Height**|Numeric, Quantity, Dimension, Height|The measurement of vertical distance.|
 
-#### Age
 
-**Description:** Ages
+### Type: Information
+##### Category: Information
 
-#### Currency
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Information**|Information|Structured data or processed knowledge transmitted or acquired about a specific entity, event, or condition.|[Dimension metadata](entity-metadata.md#information)|
 
-**Description:** Currencies
 
-#### Number
+### Type: IpAddress
+##### Category:IpAddress
 
-**Description:** Numbers without a unit
+|Entity|Tags|Detail|
+|---|---|---|
+|**IpAddress**|IpAddress|A unique numerical label assigned a device connected to a computer network using Internet Protocol.|
 
-#### NumberRange
 
-**Description:** Range of numbers
+### Type: Length
+##### Category: Quantity
 
-#### Percentage
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Length**|Numeric, Quantity, Dimension, Length|The measurement of an object or distance between two points.|[Length metadata](entity-metadata.md#length)|
 
-**Description:** Percentages
 
-#### Ordinal
+### Type: Location
+##### Category: Location
 
-**Description:** Ordinal Numbers
+|Entity|Tags|Detail|
+|---|---|---|
+|**Location**|Location|A specific point or area in physical or virtual space defined by exact coordinates, metadata, or unique identifiers that can be referenced, queried, or accessed.|
 
-#### Temperature
+### Type: NaturalEvent
+##### Category: Event
 
-**Description:** Temperatures
+|Entity|Tags|Detail|Language support|
+|---|---|---|---|
+|**NaturalEvent**|Event, EventNatural|An occurrence or phenomenon that takes place in a physical environment as a result of natural processes, without direct human intervention.|`en`|
 
-#### Dimension
 
-**Description:** Dimensions or measurements
+### Type: Number
+##### Category: Quantity
 
-This entity tag also supports tagging the entity type with the following tags:
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Number**|Numeric, Quantity, Number|A mathematical value used for counting, measuring, or labeling.|[Number metadata](entity-metadata.md#number)|
 
-|Entity tag |Details            |
-|-----------|-------------------|
-|Length     |Length of an object|
-|Weight     |Weight of an object|
-|Height     |Height of an object|
-|Speed      |Speed of an object |
-|Area       |Area of an object  |
-|Volume     |Volume of an object|
-|Information|Unit of measure for digital information|
 
-## Type: Temporal
+### Type: NumberRange
+##### Category: Quantity
 
-Dates and times of day
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**NumberRange**|Numeric, Quantity, NumberRange|A set of numbers that includes all values between a specified minimum and maximum boundary.|[NumberRange metadata](entity-metadata.md#numericrange)
 
-This entity type could be tagged by the following entity tags:
 
-#### Date
+### Type: Ordinal
+##### Category: Quantity
 
-**Description:** Calendar dates
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Ordinal**|Numeric, Ordinal|A number indicating position or order in a sequence, such as first, second, or third.|[Ordinal metadata](entity-metadata.md#ordinal)|
 
-#### Time
 
-**Description:** Times of day
+### Type: Organization
+##### Category: Organization
 
-#### DateTime
+|Entity|Tags|Detail|
+|---|---|---|
+|**Organization**|Organization|A company, institution, or group formed for a specific purpose.|
 
-**Description:** Calendar dates with time
 
-#### DateRange
+### Type: OrganizationMedical
+##### Category: Organization
 
-**Description:** Date range
+|Entity|Tags|Detail|Language support|
+|---|---|---|---|
+|**OrganizationMedical**|Organization, OrganizationMedical|An entity that delivers or facilitates healthcare or medical services.|`en`|
 
-#### TimeRange
+### Type: OrganizationSports
 
-**Description:** Time range
+|Entity|Tags|Detail|Language support|
+|---|---|---|---|
+|**OrganizationSports**|Organization, OrganizationSports|An entity that manages or promotes sports activities or teams (**Organization**).|`en`|
 
-#### DateTimeRange
+### Type: OrganizationStockExchange
+##### Category: Organization
 
-**Description:** Date Time range
+|Entity|Tags|Detail|Language support|
+|---|---|---|---|
+|**OrganizationStockExchange**|Organization, OrganizationStockExchange|An institution that manages or facilitates the trading of stocks and securities.|`en`|
 
-#### Duration
+### Type: Percentage
+##### Category: Quantity
 
-**Description:** Durations
+|Entity|Tags|Detail|
+|---|---|---|
+|**Percentage**|Numeric, Quantity, Percentage|A value expressed as a fraction of 100, representing a proportion or share.|
 
-#### SetTemporal
 
-**Description:** Set, repeated times
+### Type: Person
+##### Category: Person
 
-## Type: Event
+|Entity|Tags|Detail|
+|---|---|---|
+|**Person**|Person|An individual human being or a legal entity with rights and responsibilities.|
 
-Events with a timed period
 
-This entity type could be tagged by the following entity tags:
+### Type: PersonType
+##### Category: PersonType
 
-#### SocialEvent
+|Entity|Tags|Detail|
+|---|---|---|
+|**PersonType**|PersonType|A classification describing the role or category of a person, such as employee or customer.|
 
-**Description:** Social events
 
-#### CulturalEvent
+### Type: PhoneNumber
+##### Category: PhoneNumber
 
-**Description:** Cultural events
+|Entity|Tags|Detail|
+|---|---|---|
+|**PhoneNumber**|PhoneNumber|A unique sequence of digits assigned to a telephone line or mobile device that serves as an identifier within a communication network.|
 
-#### NaturalEvent
 
-**Description:** Natural events
+### Type: Product
+##### Category: Product
 
-## Type: Location
+|Entity|Tags|Detail|
+|---|---|---|
+|**Product**|Product|An item or service offering value and created for sale or use.|
 
-Particular point or place in physical space
 
-This entity type could be tagged by the following entity tags:
-#### GPE
+### Type: SetTemporal
+##### Category: DateTime
 
-**Description:** GeoPolitialEntity
 
-This entity tag also supports tagging the entity type with the following tags:
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Set**|DateTime, Set|A sequence of sets, where each individual set is associated with a timestamp.|[Set metadata](entity-metadata.md#set)|
 
-|Entity tag   |Details            |
-|-------------|-------------------|
-|City         |Cities             |
-|State        |States             |
-|CountryRegion|Countries/Regions  |
-|Continent    |Continents         |
+### Type: Skill
+##### Category: Skill
 
-#### Structural
+|Entity|Tags|Detail|
+|---|---|---|
+|**Skill**|Skill|The ability to perform a task or activity, acquired through training or experience.|
 
-**Description:** Manmade structures
+### Type: Speed
+##### Category: Quantity
 
-This entity tag also supports tagging the entity type with the following tags:
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Speed**|Numeric, Quantity, Dimension, Speed|The rate at which something moves or operates, typically measured in units per time.|[Speed metadata](entity-metadata.md#speed)|
 
-|Entity tag   |Details            |
-|-------------|-------------------|
-|Airport      |Airports           |
+### Type: SportsEvent
+##### Category: Event
 
-#### Geological
 
-**Description:** Geographic and natural features
+|Entity|Tags|Detail|Language support|
+|---|---|---|---|
+|**SportsEvent**|Event, EventSports|An organized competition or exhibition that involves skill or strategy typically governed by a set of rules.|`en`|
 
-This entity tag also supports tagging the entity type with the following tags:
 
-|Entity tag   |Details            |
-|-------------|-------------------|
-|River        |Rivers             |
-|Ocean        |Oceans             |
-|Desert       |Deserts            |
+### Type: State
+##### Category: Location
 
-## Type: Organization
+|Entity|Tags|Detail|
+|---|---|---|
+|**State**|Location,GPE,State|The institutional framework and governing apparatus for a defined geographical area or political entity.|
 
-Corporations, agencies, and other groups of people defined by some established organizational structure
 
-This entity type could be tagged by the following entity tags:
+### Type: Structural
+##### Category: Location
 
-#### MedicalOrganization
+|Entity|Tags|Detail|
+|---|---|---|
+|**Structural**|Location, Structural|The configuration or organizational schema of components within a system or object that define the overall architecture.|
 
-**Description:** Medical companies and groups
+### Type: Temporal
+##### Category: DateTime
 
-#### StockExchange
+|Entity|Tags|Detail|
+|---|---|---|
+|**Temporal**|Related to time or time-based changes, such as data, events, or processes that vary over time.|
 
-**Description:** Stock exchange groups
 
-#### SportsOrganization
+### Type: Temperature
+##### Category: Quantity
 
-**Description:** Sports-related organizations
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Temperature**|Numeric, Quantity, Temperature|A quantitative expression that indicates the measure of heat or cold present in an object or environment, commonly expressed in units such as degrees.|[Temperature metadata](entity-metadata.md#temperature)|
 
-## Type: Person
 
-Names of individuals
+### Type: Time
+##### Category: DateTime
 
-## Type: PersonType
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Time**|DateTime, Time|A quantifiable interval during which an event occurs, a process unfolds, or a condition persists.|[Time metadata](entity-metadata.md#time)|
 
-Human roles classified by group membership
 
-## Type: Email
+### Type: TimeRange
+##### Category: DateTime
 
-Email addresses
 
-## Type: URL
+|Entity|Tags|Detail|
+|---|---|---|
+|**TimeRange**|DateTime, TimeRange|An interval period defined by specific start and designated end times. |
 
-URLs to websites
 
-## Type: IP
+### Type: URL
+##### Category: URL
 
-Network IP addresses
 
-## Type: PhoneNumber
+|Entity|Tags|Detail|
+|---|---|---|
+|**Skill**|URL|A Uniform Resource Identifier is a string of characters that uniquely identifies a resource on the internet.|
 
-Phone numbers
 
-## Type: Product
+### Type: Volume
+##### Category: Quantity
 
-Commercial, consumable objects
 
-This entity type could be tagged by the following entity tags:
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Volume**|Numeric, Quantity, Dimension, Volume|The measure of three-dimensional space taken up by a substance or object, typically expressed in cubic units.|[Volume metadata](entity-metadata.md#volume)|
 
-#### ComputingProduct
 
-**Description:** Computing products
+### Type: Weight
+##### Category: Quantity
 
-## Type: Skill
+|Entity|Tags|Detail|MetaData|
+|---|---|---|---|
+|**Weight**|Numeric, Quantity, Dimension, Weight|The measure of the force exerted on an object due to gravity typically expressed in units like kilograms or pounds.|[Weight metadata](entity-metadata.md#weight)|
 
-Capabilities, skills, or expertise
 
----
 
 ## Next steps
 
-* [NER overview](../overview.md)
+[NER overview](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "固有表現カテゴリの再構成"
}
```

### Explanation
このコードの差分は、`named-entity-categories.md` ドキュメントにおける固有表現（NER）カテゴリと型に関する情報を再編成し、明確化したことを示しています。以下の主な変更が含まれています。

- タイトルが「Supported Named Entity Recognition (NER) entity categories and entity types」から「Named entity categories and types」に変更され、より簡潔かつ性的になりました。
- NER のプロセスに関する説明が追加され、エンティティが検出されるメカニズムについての理解を深めています。
- 新しい構成として、エンティティカテゴリとタイプの定義が強調され、カテゴリが「Location」、「Organization」、「Date」などの主要な分類を示し、タイプがより詳細な識別を提供することが明記されています。
- いくつかの情報セクションが表形式で再編され、各カテゴリごとに関連するエンティティの詳細が整理されています。
- 不要な情報が削除され、言語サポートやAPIの更新状況が一元化されています。
- API のバージョン情報の整理が行われ、特定の変更点をより明確に示しています。

全体的に、この更新はドキュメントの構造を改善し、読者がNERにおけるエンティティのカテゴリとタイプをより簡単に理解できるようになっています。

## articles/ai-services/language-service/named-entity-recognition/how-to-call.md{#item-c5709f}

<details>
<summary>Diff</summary>
````diff
@@ -40,7 +40,7 @@ When you get results from NER, you can stream the results to an application or s
 
 ## Select which entities to be returned
 
-The API attempts to detect the [defined entity types and tags](concepts/named-entity-categories.md) for a given input text language. The entity types and tags replace the categories and subcategories structure the older models use to define entities for more flexibility. You can also specify which entities are detected and returned, use the optional `includeList` and `excludeList` parameters with the appropriate entity types. The following example would detect only `Location`. You can specify one or more [entity types](concepts/named-entity-categories.md) to be returned. Given the types and tags hierarchy introduced for this version, you have the flexibility to filter on different granularity levels as so:
+The API attempts to detect the [defined entity types and tags](concepts/named-entity-categories.md) for a given input text language. The entity types and tags replace the categories and subcategories structure the older models use to define entities for more flexibility. You can also specify which entities are detected and returned, use the optional `inclusionList` and `exclusionList` parameters with the appropriate entity types. The following example would detect only `Location`. You can specify one or more [entity types](concepts/named-entity-categories.md) to be returned. Given the types and tags hierarchy introduced for this version, you have the flexibility to filter on different granularity levels as so:
 
 **Input:**
 
@@ -52,7 +52,7 @@ The API attempts to detect the [defined entity types and tags](concepts/named-en
     "kind": "EntityRecognition",
     "parameters": 
     {
-        "includeList" :
+        "inclusionList" :
         [
             "Location"
         ]
@@ -78,25 +78,25 @@ The above examples would return entities falling under the `Location` entity typ
 
     "parameters": 
     {
-        "includeList" :
+        "inclusionList" :
         [
             "GPE"
         ]
     }
     
 ```
 
-This method returns all `Location` entities only falling under the `GPE` tag and ignore any other entity falling under the `Location` type that is tagged with any other entity tag such as `Structural` or `Geological` tagged `Location` entities. We can also further analyze our results by using the `excludeList` parameter. `GPE` tagged entities could be tagged with the following tags: `City`, `State`, `CountryRegion`, `Continent`. We could, for example, exclude `Continent` and `CountryRegion` tags for our example:
+This method returns all `Location` entities only falling under the `GPE` tag and ignore any other entity falling under the `Location` type that is tagged with any other entity tag such as `Structural` or `Geological` tagged `Location` entities. We can also further analyze our results by using the `exclusionList` parameter. `GPE` tagged entities could be tagged with the following tags: `City`, `State`, `CountryRegion`, `Continent`. We could, for example, exclude `Continent` and `CountryRegion` tags for our example:
 
 ```bash
 
     "parameters": 
     {
-        "includeList" :
+        "inclusionList" :
         [
             "GPE"
         ],
-        "excludeList": :
+        "exclusionList": :
         [
             "Continent",
             "CountryRegion"
@@ -105,7 +105,7 @@ This method returns all `Location` entities only falling under the `GPE` tag and
     
 ```
 
-Using these parameters we can successfully filter on only `Location` entity types, since the `GPE` entity tag included in the `includeList` parameter, falls under the `Location` type. We then filter on only Geopolitical entities and exclude any entities tagged with `Continent` or `CountryRegion` tags.
+Using these parameters we can successfully filter on only `Location` entity types, since the `GPE` entity tag included in the `inclusionList` parameter, falls under the `Location` type. We then filter on only Geopolitical entities and exclude any entities tagged with `Continent` or `CountryRegion` tags.
 
 ## Supported output attributes
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティ検出リストのパラメータ名称変更"
}
```

### Explanation
このコードの差分は、`how-to-call.md` ドキュメントにおけるエンティティ検出の結果を指定するためのパラメータの名称を変更したことを示しています。具体的には、次のような変更が行われています。

- `includeList` と `excludeList` というパラメータ名が、それぞれ `inclusionList` と `exclusionList` に変更されています。この変更は、一貫性のある命名を促進し、APIの利用者がパラメータの機能をより理解しやすくすることを目的としています。
- 他の記述はそのまま保たれており、エンティティの選択がどのように行われるかや、実際のリクエストの構造についての説明が維持されています。
- 具体的な例では、`Location` エンティティタイプと、それに関連するタグの使用に関するコードスニペットが示されていますが、パラメータ名の変更に伴う影響はありません。

この更新により、小さな修正ですが、APIの適切な利用に必要な情報の再確認が促され、ユーザーがより効果的にエンティティのフィルタリングを行えるようになっています。


