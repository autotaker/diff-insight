---
date: '2026-03-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2da5224...MicrosoftDocs:0663ebe
summary: このコード差分は、MicrosoftのAIサービスにおける言語サービスの地域サポートに関するドキュメントの更新を示しています。主な変更ポイントは、`regional-support.md`に新しい地域ごとのサポート情報のテーブルが追加され、`overview.md`に地域の可用性に関するセクションが追加されたことです。これにより、カスタム質問応答機能の地域ごとのサポート状況が明確になり、ユーザーが利用可能な地域を一目で確認できるようになります。また、ドキュメントの日付も最新情報に更新されました。全体として、これらの改善は地域的な可用性を透明にし、ユーザーエクスペリエンスを向上させることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2da5224...MicrosoftDocs:0663ebe){target="_blank"}

# ハイライト
このコード差分は、主にMicrosoftのAIサービスにおける言語サービスの地域サポートに関するドキュメントの更新を示しています。変更は二つのドキュメントに渡っています：

1. `regional-support.md`：新しい地域ごとのサポート情報のテーブルが追加されました。
2. `overview.md`：地域の可用性に関するセクションが追加されました。

## 新しい機能
- カスタム質問応答機能の地域ごとのサポート状況を示すテーブルが追加され、ユーザーがどの地域でこの機能が利用可能かを明確に理解できるようになりました。

## 破壊的変更
- 特にありません。

## その他の更新
- ドキュメントの日付がそれぞれ最新情報に基づき更新されました。

# インサイト
これらの変更は、AIサービスにおける言語サービスのユーザー向けに地域的な可用性を透明かつ明確にすることを目的としています。特に、カスタム質問応答機能がどの地域でサポートされているかを具体的に示すことにより、ユーザーは自分がいる地域での利用可能性を一目で確認できるようになりました。

### 地域サポートに関する明確化
地域ごとのサポート情報が追加されたことにより、ユーザーは自分が利用する地域でどのようなサポート体制が取られているかを詳細に把握できます。これにより、導入前に地域的制約を確認することができ、サービス選択時の計画が立てやすくなります。

### 利用可能性を高めるためのリンク追加
`overview.md`の中で、サービスが提供されている地域に関するリンクが提供されたことは、ユーザーが迅速に情報にアクセスする手助けになります。この追加により、サービスの導入や利用計画の策定が円滑に行えるようになっています。

総じて、これらのドキュメントの改善は、ユーザーが地理的制約を考慮に入れた上でサービスをフルに活用できるようにするための重要なステップといえます。このような地域可用性の情報を提供することは、サービスの透明性の向上に寄与し、ユーザーエクスペリエンスを向上させるものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [regional-support.md](#item-5becd3) | minor update | 地域によるサポートに関する更新 | modified | 42 | 1 | 43 | 
| [overview.md](#item-631b23) | minor update | 質問応答サービスの概要に地域の可用性を追加 | modified | 6 | 1 | 7 | 


# Modified Contents
## articles/ai-services/language-service/concepts/regional-support.md{#item-5becd3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: concept-article
-ms.date: 11/18/2025
+ms.date: 03/06/2026
 ms.author: lajanuar
 ms.custom: references_regions
 ---
@@ -189,6 +189,47 @@ Custom text classification is only available in some Azure regions. Some regions
 |WestUS|✓|✓|
 |WestUS2|✓|✓|
 
+## Custom question and answering
+
+| Region | Authoring | Prediction |
+| --- | --- | --- |
+| AustraliaEast | ✓ | ✓ |
+| BrazilSouth | ✓ | ✓ |
+| CanadaCentral | ✓ | ✓ |
+| CentralIndia | ✓ | ✓ |
+| CentralUS | ✓ | ✓ |
+| ChinaEast2 | ✓ | ✓ |
+| ChinaNorth2 | ✓ | ✓ |
+| ChinaNorth3 | ✓ | ✓ |
+| EastAsia | ✓ | ✓ |
+| EastUS | ✓ | ✓ |
+| EastUS2 | ✓ | ✓ |
+| FranceCentral | ✓ | ✓ |
+| GermanyWestCentral | ✓ | ✓ |
+| JapanEast | ✓ | ✓ |
+| JapanWest | ✓ | ✓ |
+| JioIndiaWest | ✓ | ✓ |
+| KoreaCentral | ✓ | ✓ |
+| NorthCentralUS | ✓ | ✓ |
+| NorthEurope | ✓ | ✓ |
+| NorwayEast | ✓ | ✓ |
+| QatarCentral | ✓ | ✓ |
+| SouthAfricaNorth | ✓ | ✓ |
+| SouthCentralUS | ✓ | ✓ |
+| SouthEastAsia | ✓ | ✓ |
+| SwedenCentral | ✓ | ✓ |
+| SwitzerlandNorth | ✓ | ✓ |
+| SwitzerlandWest | ✓ | ✓ |
+| UaeNorth | ✓ | ✓ |
+| UKSouth | ✓ | ✓ |
+| USGovArizona | ✓ | ✓ |
+| USGovVirginia | ✓ | ✓ |
+| WestCentralUS | ✓ | ✓ |
+| WestEurope | ✓ | ✓ |
+| WestUS | ✓ | ✓ |
+| WestUS2 | ✓ | ✓ |
+| WestUS3 | ✓ | ✓ |
+
 ### Next steps
 
 * [Language support](./language-support.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域によるサポートに関する更新"
}
```

### Explanation
この変更では、`regional-support.md`ドキュメントが更新され、主に新しい情報が追加されました。具体的には、カスタム質問応答機能が利用可能な地域に関するテーブルが追加され、各地域での著作および予測のサポート状況が示されています。この変更により、ユーザーはどの地域でこの機能が利用できるかをより明確に理解できるようになります。また、ドキュメントの日付が2025年11月18日から2026年3月6日に更新されました。

追加された情報には、オーストラリア東部やブラジル南部など、さまざまな地域の詳細が含まれています。このように地域ごとのサポート状況を明確にすることは、利用者にとって非常に有益です。全体として、この更新により、ユーザーが利用可能なサービスについてより正確な情報を得られるようになりました。

## articles/ai-services/language-service/question-answering/overview.md{#item-631b23}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: laujan
 ms.author: lajanuar
 recommendations: false
 ms.topic: overview
-ms.date: 12/10/2025 
+ms.date: 03/06/2026
 keywords: "low code chat bots, multi-turn conversations"
 ms.custom: language-service-question-answering
 ---
@@ -44,6 +44,11 @@ Choose from multiple development approaches based on your technical requirements
   * [.NET (C#) packages](https://www.nuget.org/packages/Azure.AI.Language.QuestionAnswering/) - Runtime and authoring SDKs for C# applications
   * [Python packages](https://pypi.org/project/azure-ai-language-questionanswering/) - Runtime and authoring SDKs for Python applications
 
+
+## Regional availability
+
+For supported regions and availability, see [Custom question answering regional support](../concepts/regional-support.md#custom-question-and-answering).
+
 ## Next steps
 
 * [Quickstart: Create and deploy a CQA project](./quickstart/sdk.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "質問応答サービスの概要に地域の可用性を追加"
}
```

### Explanation
この変更では、`overview.md`ドキュメントが更新され、主に地域の可用性に関する情報が追加されました。具体的には、「地域の可用性」という新しいセクションが設けられ、カスタム質問応答機能がサポートされている地域とその可用性に関するリンクが提供されています。この情報は、ユーザーがサービスを利用する際の地理的要因を考慮するのに役立ちます。

さらに、ドキュメントの日付が2025年12月10日から2026年3月6日に更新されました。また、他の若干のキーワードや情報も含まれていますが、全体としては地域の可用性情報の追加が主要な変更点となっています。これにより、読者はカスタム質問応答機能がどの地域で利用可能であるかを一目で把握できるようになっています。


