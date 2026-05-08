---
date: '2026-05-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7864579...MicrosoftDocs:7184c17
summary: 今回の修正では、文書のバージョン情報や状態を明確にするための更新が行われ、特に退役中のバージョンを示す新しいアイコンが追加されました。このアイコンにより、ユーザーは各バージョンの状態をより直感的に理解できるようになります。また、認証方式の名称変更やドキュメント目次の再構成も行われています。全体として、ユーザーに必要な情報をよりわかりやすく提供し、ドキュメントの構成を改善することに重点が置かれています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7864579...MicrosoftDocs:7184c17){target="_blank"}

<format>
# Highlights
今回の修正では、いくつかの文書のバージョン情報、状態、および新しいアイコンの追加が行われました。特に、新たなアイコンは退役中のバージョンを示すためのものであり、バージョン管理に関する明確な情報提供が強調されています。そのほかにも、認証方式の名称変更やドキュメント目次の再構成などが行われています。

## New features
- `retire-icon.png` という新しいアイコンが追加され、退役中のバージョンを視覚的に示すようになりました。これにより、ユーザーは各バージョンのステータスをより直感的に理解できます。

## Breaking changes
- 特に大きな破壊的変更はありませんが、認証方式の名称変更などにより、既存のドキュメントには影響があります。

## Other updates
- ドキュメントファイルでのアイコン色の変更（緑から赤）を通じて、退役中のバージョンの状態をわかりやすく表示するようになりました。
- サポート終了日についての情報が新たに追加され、各バージョンの移行時期についての情報が更新されました。
- 認証方式の「Azure Active Directory」が「Microsoft Entra ID」に名称変更され、関連する変更が反映されました。
- ドキュメント目次が整理され、多くの項目が追加・削除されています。

# Insights
この差分変更は、主にドキュメントにおけるバージョン管理の明確化、ユーザーへの必要な情報提供の改善、そしてドキュメント構成の整理に焦点を当てています。具体的には古いバージョンが「退役中」であることを示すため、アイコンの色を緑から赤に変更しました。この変更は、ユーザーが使用するバージョンのサポート状況を把握しやすくするためのものです。

新たに追加されたアイコンファイルは、ドキュメント内での視覚的な情報提供を助け、ユーザーがバージョン状態をより簡単に理解できるように設計されています。認証方式の名称変更に伴うドキュメント更新は、ユーザーに最新の用語を提供し、混乱を避けるためのものです。また、「新しい名称に基づく認証方式」と「従来のローカル認証」の違いが明示されており、どのように適切な設定を行うかの案内が記載されているなど、ユーザーの理解を助ける工夫が見られます。

目次の更新に関しては、多くの項目が追加され、配列が再編成されていることから、ドキュメント全体の構成が見直され、ユーザーに対する情報のアクセス性や可視性が改善されています。

これらの更新により、ユーザーは無効となったバージョンの情報に惑わされることなく、自身の利用しているAPIやSDKがどのような状態にあるかを確認しやすくなり、必要に応じて適切なバージョンに移行することが推奨されます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [applies-to-v21.md](#item-fa19ef) | minor update | コンテンツのバージョン情報の更新 | modified | 1 | 1 | 2 | 
| [applies-to-v30-v21.md](#item-5311b0) | minor update | コンテンツのバージョンステータスの更新 | modified | 1 | 1 | 2 | 
| [applies-to-v30.md](#item-0f6a07) | minor update | コンテンツのバージョンおよびステータスの更新 | modified | 1 | 1 | 2 | 
| [applies-to-v31-v30-v21.md](#item-e8f78f) | minor update | コンテンツのバージョンおよびステータスの更新 | modified | 1 | 1 | 2 | 
| [applies-to-v31-v30.md](#item-ac265d) | minor update | コンテンツのバージョンおよびステータスの更新 | modified | 1 | 1 | 2 | 
| [applies-to-v31.md](#item-5f3c5a) | minor update | コンテンツのバージョン表記の更新 | modified | 1 | 1 | 2 | 
| [applies-to-v40-v31-v30-v21.md](#item-3ca431) | minor update | コンテンツのバージョンステータスの更新 | modified | 1 | 1 | 2 | 
| [applies-to-v40-v31-v30.md](#item-cb0a7f) | minor update | バージョン表記の用語の変更 | modified | 1 | 1 | 2 | 
| [applies-to-v40.md](#item-94c322) | minor update | バージョン表記の用語とステータスの変更 | modified | 1 | 1 | 2 | 
| [retire-icon.png](#item-b82e55) | new feature | 新しいアイコンの追加 | added | 0 | 0 | 0 | 
| [overview.md](#item-4e36ba) | minor update | ドキュメントの更新と重要な情報の追加 | modified | 8 | 3 | 11 | 
| [get-started-studio.md](#item-b2798e) | minor update | 認証方式の名称変更 | modified | 2 | 2 | 4 | 
| [toc.yml](#item-81aa7b) | minor update | ドキュメント目次の更新と整理 | modified | 57 | 52 | 109 | 
| [migration-guide-overview.md](#item-49f49c) | minor update | マイグレーションガイドの名称変更と内容の更新 | renamed | 17 | 2 | 19 | 
| [sdk-overview-v3-0.md](#item-f82845) | minor update | SDK概要の更新とサポート期限の明示 | modified | 8 | 3 | 11 | 
| [sdk-overview-v4-0.md](#item-d59a82) | minor update | SDK概要の更新日付の変更 | modified | 1 | 1 | 2 | 
| [whats-new.md](#item-1ec8d3) | minor update | 機能更新とサポート終了情報の追加 | modified | 4 | 3 | 7 | 


# Modified Contents
## articles/ai-services/document-intelligence/includes/applies-to-v21.md{#item-fa19ef}

<details>
<summary>Diff</summary>
````diff
@@ -9,4 +9,4 @@ ms.topic: include
 ms.date: 11/18/2025
 ---
 
-**This content applies to:** ![checkmark](../media/yes-icon.png) **v2.1** | **Latest version:** ![blue-checkmark](../media/blue-yes-icon.png) [**v4.0 (GA)**](?view=doc-intel-4.0.0&preserve-view=tru)
+**This content applies to:** ![red-checkmark](../media/retire-icon.png) **v2.1** | **Latest version:** ![blue-checkmark](../media/blue-yes-icon.png) [**v4.0 (GA)**](?view=doc-intel-4.0.0&preserve-view=tru)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツのバージョン情報の更新"
}
```

### Explanation
この変更は、ドキュメントのバージョン情報を更新するためのマイナーな変更です。具体的には、`applies-to-v21.md`ファイルの内容において、v2.1の適用情報に使われるチェックマークのアイコンが変更されました。以前は緑色のチェックマークが使用されていましたが、現在は赤色のチェックマークに変更されています。この修正は、の最新情報としての明確性を高めることを目的としています。変更点は合計で2箇所で、1行が追加され、1行が削除されています。

## articles/ai-services/document-intelligence/includes/applies-to-v30-v21.md{#item-5311b0}

<details>
<summary>Diff</summary>
````diff
@@ -9,4 +9,4 @@ ms.topic: include
 ms.date: 11/18/2025
 ---
 
-**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** ![checkmark](../media/yes-icon.png) **v2.1 (GA)**
+**This content applies to:** ![red-checkmark](../media/retire-icon.png) **v3.0 (retiring)** ![red-checkmark](../media/retire-icon.png) **v2.1 (retiring)**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツのバージョンステータスの更新"
}
```

### Explanation
この変更は、バージョンステータスを更新するためのマイナーな変更です。`applies-to-v30-v21.md`ファイル内で、v3.0およびv2.1の適用情報の記述が変更されました。以前は両方のバージョンに対して緑色のチェックマークが表示されていましたが、現在は両方のバージョンが「退役中」（retiring）であることを示すために赤色のチェックマークに変更されています。この変更により、利用者に対して適用されるバージョンの状態をより明確に伝えることが目的です。全体として、2箇所の変更が行われ、1行が追加され、1行が削除されています。

## articles/ai-services/document-intelligence/includes/applies-to-v30.md{#item-0f6a07}

<details>
<summary>Diff</summary>
````diff
@@ -9,4 +9,4 @@ ms.topic: include
 ms.date: 11/18/2025
 ---
 
-**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (GA)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](../media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true) | **Previous version:** ![blue-checkmark](../media/blue-yes-icon.png) [v2.1](?view=doc-intel-2.1.0&preserve-view=true)
+**This content applies to:** ![red-checkmark](../media/retire-icon.png) **v3.0 (retiring)** | **Latest versions:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (GA)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](../media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true) | **Previous version:** ![blue-checkmark](../media/blue-yes-icon.png) [v2.1 (retiring)](?view=doc-intel-2.1.0&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツのバージョンおよびステータスの更新"
}
```

### Explanation
この変更は、ドキュメントにおけるバージョンおよびステータスの更新を目的としたマイナーな変更です。`applies-to-v30.md`ファイルの内容が変更され、v3.0に関する記述が「退役中」（retiring）であることを示す赤色のチェックマークに更新されました。また、v2.1も退役中として表示されるように変更されています。最新バージョンとしてv4.0とv3.1の情報はそのまま維持されています。この修正により、コンテンツに関連するバージョンの状態がより明確に表現されます。変更は合計で2箇所で、1行が追加され、1行が削除されています。

## articles/ai-services/document-intelligence/includes/applies-to-v31-v30-v21.md{#item-e8f78f}

<details>
<summary>Diff</summary>
````diff
@@ -9,4 +9,4 @@ ms.topic: include
 ms.date: 11/18/2025
 ---
 
-**This content applies to:**![checkmark](../media/yes-icon.png) **v3.1 (GA)** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** ![checkmark](../media/yes-icon.png) **v2.1 (GA)**
+**This content applies to:**![checkmark](../media/yes-icon.png) **v3.1 (GA)** ![red-checkmark](../media/retire-icon.png) **v3.0 (retiring)** ![red-checkmark](../media/retire-icon.png) **v2.1 (retiring)**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツのバージョンおよびステータスの更新"
}
```

### Explanation
この変更は、ドキュメントにおけるバージョンおよびステータスの更新を目的としたマイナーな変更です。`applies-to-v31-v30-v21.md`ファイルの内容が変更され、v3.0およびv2.1に関する記述が「退役中」（retiring）であることを示す赤色のチェックマークに変更されました。一方で、v3.1は引き続き「一般提供中」（GA）として表示されており、利用者に対して適用されるバージョンの状態を明確に示しています。この変更により、各バージョンの現在の状況が適切に反映されています。変更は合計で2箇所行われ、1行が追加され、1行が削除されています。

## articles/ai-services/document-intelligence/includes/applies-to-v31-v30.md{#item-ac265d}

<details>
<summary>Diff</summary>
````diff
@@ -9,4 +9,4 @@ ms.topic: include
 ms.date: 11/18/2025
 ---
 
-**This content applies to:**![checkmark](../media/yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=true) ![checkmark](../media/yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=true) **Earlier version:** ![blue-checkmark](../media/blue-yes-icon.png) [v2.1](?view=doc-intel-2.1.0&preserve-view=true)
+**This content applies to:**![checkmark](../media/yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=true) ![red-checkmark](../media/retire-icon.png) [**v3.0 (retiring)**](?view=doc-intel-3.0.0&preserve-view=true) **Earlier version:** ![red-checkmark](../media/retire-icon.png) [v2.1 (retiring)](?view=doc-intel-2.1.0&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツのバージョンおよびステータスの更新"
}
```

### Explanation
この変更は、ドキュメントにおけるバージョンおよびそのステータスの更新を狙ったマイナーな修正です。`applies-to-v31-v30.md`ファイルの内容が変更され、v3.0とv2.1の状態が「退役中」として赤色のチェックマークで示されるようになりました。具体的には、v3.0は「退役中」（retiring）として更新され、v2.1も同様に表示されます。一方で、v3.1は引き続き「一般提供中」（GA）として表示されています。この変更により、各バージョンの適用状況が明確に反映され、ユーザーに対して重要な情報が提供されます。変更は合計で2箇所行われ、1行が追加され、1行が削除されています。

## articles/ai-services/document-intelligence/includes/applies-to-v31.md{#item-5f3c5a}

<details>
<summary>Diff</summary>
````diff
@@ -9,4 +9,4 @@ ms.topic: include
 ms.date: 11/18/2025
 ---
 
-**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (GA)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true) ![blue-checkmark](../media/blue-yes-icon.png) [**v2.1**](?view=doc-intel-2.1.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (GA)**](?view=doc-intel-4.0.0&preserve-view=true) | **Prior versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true) ![blue-checkmark](../media/blue-yes-icon.png) [**v2.1**](?view=doc-intel-2.1.0&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツのバージョン表記の更新"
}
```

### Explanation
この変更は、ドキュメントにおけるバージョン表記のマイナーな更新を目的とした修正です。`applies-to-v31.md`ファイルの内容が変更され、古いバージョンが「Prior versions」として示されるようになりました。具体的には、v3.0およびv2.1はそれぞれ「Previous versions」から「Prior versions」に表記が変更されました。v3.1は引き続き「一般提供中」（GA）として表示されており、最新バージョンのv4.0も同様に表示されています。この変更により、ユーザーに各バージョンの適用状態が一貫した形式で伝えられるようになっています。変更は合計で2箇所行われ、1行が追加され、1行が削除されています。

## articles/ai-services/document-intelligence/includes/applies-to-v40-v31-v30-v21.md{#item-3ca431}

<details>
<summary>Diff</summary>
````diff
@@ -9,4 +9,4 @@ ms.topic: include
 ms.date: 11/18/2025
 ---
 
-**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (GA)** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** ![checkmark](../media/yes-icon.png) **v2.1 (GA)**
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (GA)** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** ![red-checkmark](../media/retire-icon.png) **v3.0 (retiring)** ![red-checkmark](../media/retire-icon.png) **v2.1 (retiring)**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツのバージョンステータスの更新"
}
```

### Explanation
この変更は、ドキュメントにおけるバージョンステータスの更新を目的としたマイナーな修正です。`applies-to-v40-v31-v30-v21.md`ファイルの内容が変更され、v3.0およびv2.1が「退役中」（retiring）として赤色のチェックマークで示されるようになりました。具体的には、v3.0とv2.1が新たに「退役中」として表示され、ユーザーに対してこれらのバージョンがもはやサポートされないことが明示されます。一方、v4.0およびv3.1は引き続き「一般提供中」（GA）として示されています。この修正により、各バージョンの使用状況がより明確に伝えられるようになります。変更は合計で2箇所行われ、1行が追加され、1行が削除されています。

## articles/ai-services/document-intelligence/includes/applies-to-v40-v31-v30.md{#item-cb0a7f}

<details>
<summary>Diff</summary>
````diff
@@ -9,4 +9,4 @@ ms.topic: include
 ms.date: 11/18/2025
 ---
 
-**This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (GA)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru) 
+**This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (GA)** | **Prior versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![red-checkmark](../media/retire-icon.png) [**v3.0 (retiring)**](?view=doc-intel-3.0.0&preserve-view=tru)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バージョン表記の用語の変更"
}
```

### Explanation
この変更は、ドキュメントにおけるバージョン表記の用語を改善するためのマイナーな修正です。ファイル`applies-to-v40-v31-v30.md`内のコンテンツが更新され、以前「Previous versions」と表現されていた箇所が「Prior versions」に変更されました。さらに、v3.0は「退役中」（retiring）として赤色のチェックマークで示されるようになりましたが、v4.0およびv3.1は引き続き「一般提供中」（GA）として示されています。この変更により、バージョンの適用状態がさらに明確になり、ユーザーに対して正確な情報が提供されることを目的としています。変更は合計で2箇所行われ、1行が追加され、1行が削除されています。

## articles/ai-services/document-intelligence/includes/applies-to-v40.md{#item-94c322}

<details>
<summary>Diff</summary>
````diff
@@ -9,4 +9,4 @@ ms.topic: include
 ms.date: 11/18/2025
 ---
 
-**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (GA)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru) ![blue-checkmark](../media/blue-yes-icon.png) [**v2.1 (GA)**](?view=doc-intel-2.1.0&preserve-view=tru)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (GA)** | **Prior versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![red-checkmark](../media/retire-icon.png) [**v3.0 (retiring)**](?view=doc-intel-3.0.0&preserve-view=tru) ![red-checkmark](../media/retire-icon.png) [**v2.1 (retiring)**](?view=doc-intel-2.1.0&preserve-view=tru)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バージョン表記の用語とステータスの変更"
}
```

### Explanation
この変更は、ドキュメント内のバージョン表記とそのステータスに関するマイナーな修正です。`applies-to-v40.md`ファイルの内容が更新され、「Previous versions」という表現が「Prior versions」に変更されました。また、v3.0とv2.1のバージョンが新たに「退役中」（retiring）と表示されるようになり、赤色のチェックマークが追加されています。v4.0およびv3.1は引き続き「一般提供中」（GA）として示されています。この修正は、ユーザーに対して各バージョンの適用状態をより明確に伝えることを目的としており、変更は合計で2つの箇所で行われ、1行が追加され、1行が削除されています。

## articles/ai-services/document-intelligence/media/retire-icon.png{#item-b82e55}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しいアイコンの追加"
}
```

### Explanation
この変更は、ドキュメントに新しいアイコンファイルが追加されたことを示しています。`retire-icon.png`という名前のファイルが、`articles/ai-services/document-intelligence/media/`ディレクトリに追加されました。このアイコンは、退役中のバージョンを示すために使用されることが予想され、ドキュメント内でのバージョンの状態を視覚的に表す役割を果たします。変更は追加のみで、削除や編集は行われていません。このアイコンの追加により、ユーザーは各バージョンの適用状態をより直感的に理解できるようになります。

## articles/ai-services/document-intelligence/overview.md{#item-4e36ba}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: overview
-ms.date: 11/18/2025
+ms.date: 05/06/2026
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
 ---
@@ -21,7 +21,6 @@ monikerRange: '<=doc-intel-4.0.0'
 
  :::moniker range="doc-intel-4.0.0"
 
-
 [!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
 
 :::moniker-end
@@ -41,6 +40,12 @@ monikerRange: '<=doc-intel-4.0.0'
 
 :::moniker-end
 
+> [!IMPORTANT]
+>
+> * **Document Intelligence REST API v2.1** reaches end of support on **September 15, 2027**.
+> * **Document Intelligence REST API 2022-08-31 v3.0** reaches end of support on **March 30, 2029**.
+> * To avoid production disruption, migrate now to **Azure Document Intelligence 2024-11-30 v4.0**. For more information, see [**Document Intelligence migration guide**](versioning/migration-guide-overview.md).
+
 Azure Document Intelligence in Foundry Tools is a cloud-based [Foundry Tools](../../ai-services/index.yml) service that you can use to build intelligent document processing solutions. Massive amounts of data, spanning various data types, are stored in forms and documents. You can use Azure Document Intelligence to effectively manage the speed at which data is collected and processed. Azure Document Intelligence is key to improved operations, informed data-driven decisions, and enlightened innovation. For information on region access, see [Product availability by region](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/table).</br></br>
 
 | ✔️ [Document analysis models](#document-analysis-models) | ✔️ [Prebuilt models](#prebuilt-models) | ✔️ [Custom models](#custom-model-overview) |
@@ -635,7 +640,7 @@ To learn more about each model and browse the API references, use the links in t
 
 :::moniker range=">=doc-intel-3.0.0"
 
-* [Choose a Document Intelligence model]().
+* [Choose a Document Intelligence model](concept/choose-model-feature.md).
 * Process your own forms and documents with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 * Finish a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true), and then create a document processing app in the development language of your choice.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの更新と重要な情報の追加"
}
```

### Explanation
この変更は、`overview.md`ファイルにおいて複数の内容が更新されたことを示しています。主な変更点は、日付の更新、情報の追加、テキストの整理です。具体的には、ドキュメントインテリジェンスのREST APIに関する重要なサポート終了日の通知が加えられ、APIのバージョンごとのサポート終了日や移行を促す内容が新たに記載されています。この情報はユーザーにとって非常に重要であり、使用中のバージョンからの移行を促進するためのものです。

また、古い日付（2025年）から新しい日付（2026年）への更新も行われました。さらに、文中の参照リンクが改訂され、いくつかの行が整理されています。これにより、ドキュメント全体の可読性や情報の正確性が向上し、より明確な指示が提供されています。この変更に伴い、合計で11箇所の変更が行われており、8行が追加され、3行が削除されています。

## articles/ai-services/document-intelligence/quickstarts/get-started-studio.md{#item-b2798e}

<details>
<summary>Diff</summary>
````diff
@@ -26,7 +26,7 @@ monikerRange: '>=doc-intel-3.0.0'
 > [!TIP]
 > Create a Microsoft Foundry resource if you plan to access multiple Foundry Tools under a single endpoint/key. For Document Intelligence access only, create a Document Intelligence resource. You need a single-service resource if you intend to use [Microsoft Entra authentication](/azure/active-directory/authentication/overview-authentication).
 >
-> Document Intelligence now supports Azure Active Directory token authentication in addition to local (key-based) authentication when you access Document Intelligence resources and storage accounts. Follow the instructions to set up correct access roles, especially if your resources are applied with the `DisableLocalAuth` policy.
+> Document Intelligence now supports Microsoft Entra ID token authentication in addition to local (key-based) authentication when you access Document Intelligence resources and storage accounts. Follow the instructions to set up correct access roles, especially if your resources are applied with the `DisableLocalAuth` policy.
 
 There are added prerequisites for using custom models in Document Intelligence Studio. For step-by-step guidance, see [Document Intelligence Studio custom projects](studio-custom-project.md).
 
@@ -42,7 +42,7 @@ For more information, see the following guidance:
   * [Disable local authentication for Foundry Tools](../../disable-local-auth.md)
   * [Prevent Shared Key authorization for an Azure Storage account](/azure/storage/common/shared-key-authorization-prevent)
 
-If local (key-based) authentication is disabled for your Document Intelligence service resource, be sure to obtain the Cognitive Services User role and your Azure Active Directory token to authenticate requests in Document Intelligence Studio. The Contributor role allows you to list only keys but doesn't give you permission to use the resource when key access is disabled.
+If local (key-based) authentication is disabled for your Document Intelligence service resource, be sure to obtain the Cognitive Services User role and your Microsoft Entra ID token to authenticate requests in Document Intelligence Studio. The Contributor role allows you to list only keys but doesn't give you permission to use the resource when key access is disabled.
 
 #### Designate role assignments
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "認証方式の名称変更"
}
```

### Explanation
この変更は、`get-started-studio.md`ファイルにおいて、Document Intelligenceに関連する認証方法に関する言及が更新されたことを示しています。主に、"Azure Active Directory"が"Microsoft Entra ID"に名称変更されたことによるもので、2つの行が追加され、2つの行が削除されています。この変更に伴い、ユーザーがドキュメントインテリジェンスリソースとストレージアカウントにアクセスする際の認証方式の理解を促進することを目的としています。

具体的には、Microsoft Entra ID トークン認証が、従来のローカル（キーごとの）認証に加えてサポートされることに関する情報が強調されています。また、ローカル認証が無効化されている場合には、正しい役割（Cognitive Services User役割）の取得が必要であることの注意喚起も引き続き明記されています。これにより、ユーザーは新しい認証方式に基づいてアクセス設定を適切に行うための指示が提供されます。全体として、この変更はドキュメントの正確性と最新性を高めています。

## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ items:
       - name:  "SDK targets: REST API v2.1 (GA)"
         displayName: get started, installation, downloads, formRecognizerClientClient, form recognizer client, Azure AD, Azure Active Directory, identity, changelog, package, version,AzureKeyCredential, Azure key credential, key, endpoint
         href: v21/sdk-overview-v2-1.md
-  - name: Changelog and migration guide
+  - name: Changelog
     displayName: latest, update, beta, package, preview, version
     href: changelog-release-history.md
   - name: Frequently asked questions (FAQ)
@@ -190,8 +190,13 @@ items:
   - name: Create SAS tokens for storage containers
     displayName: blob, delegation, shared, explorer
     href:  authentication/create-sas-tokens.md
-  - name: "SDK Migration guides"
-    items:
+- name: Migration guides
+  items:
+  - name: "Migration guide overview"
+    displayName: get started, confidence, bounding box, boundingBox, polygon, analyze, AnalyzeResult, train, build, sas, compose, copy
+    href: v3-1-migration-guide.md
+  - name: SDK migration guides
+    items:  
     - name: ".NET/C# SDK"
       href: https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/MigrationGuide.md
     - name: Java SDK
@@ -200,52 +205,52 @@ items:
       href: https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/documentintelligence/ai-document-intelligence-rest/MIGRATION-FR_v4-DI_v1.md
     - name: Python SDK
       href: https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/MIGRATION_GUIDE.md
-  - name: "Migration guide: 2023—07—31 latest (GA)"
-    displayName: get started, confidence, bounding box, boundingBox, polygon, analyze, AnalyzeResult, train, build, sas, compose, copy
-    href: v3-1-migration-guide.md
-  - name: Custom models
-    items:
-    - name: Build a custom extraction model
-      displayName: tables, labels, ocr, input, train, training, sets, testing
-      href: how-to-guides/build-a-custom-model.md
-    - name: Build a custom classification model
-      displayName: custom, classifier, splitter
-      href: how-to-guides/build-a-custom-classifier.md
-    - name: Project sharing with custom models
-      displayName: project, share, sharing
-      href: how-to-guides/project-share-custom-models.md
-    - name: Compose custom extraction models
-      displayName: custom, models, modelId, model ID, train, dataset, data set, label, ocr, upload
-      href: how-to-guides/compose-custom-models.md
-    - name: Deploy the sample-labeling tool
-      displayName: FOTT, migration, containers, docker
-      href: v21/deploy-label-tool.md
-    - name: Train a custom model with the sample-labeling tool
-      displayName: FOTT, migration, containers, docker
-      href: v21/label-tool.md
-    - name: Use table tags to train your custom model
-      displayName: FOTT, migration, dynamic
-      href: v21/supervised-table-tags.md
-  - name: Back up and recover models
-    displayName: disaster, recovery, region, copy, modelId, model ID
-    href: disaster-recovery.md
-  - name: Configure secure communications
-    items:
-    - name: Set up Virtual Networks
-      displayName: firewall, security, subdomain, VNet, virtual network, az, regions, cli
-      href: ../../ai-services/cognitive-services-virtual-networks.md?context=/azure/ai-services/document-intelligence/context/context
-    - name: Create and use managed identities
-      displayName: azure RBAC, role based access control, sas, private, assigned, system assigned, role, blob
-      href: authentication/managed-identities.md
-    - name: Configure managed identities with private endpoints
-      displayName: Azure RBAC, role based access control, sas, private, assigned, system assigned, role, blob, virtual, firewalls, VNet, virtual networks, endpoints, storage
-      href: authentication/managed-identities-secured-access.md
-    - name: Use customer-managed keys
-      displayName: encrypt, encryption, key vault
-      href: authentication/encrypt-data-at-rest.md
-    - name: Use Microsoft Entra authentication
-      displayName: headers, subscription, access token, azure active directory, subdomain, role, service principal
-      href: ../../ai-services/authentication.md?context=/azure/ai-services/document-intelligence/context/context
+
+
+- name: Custom models
+  items:
+  - name: Build a custom extraction model
+    displayName: tables, labels, ocr, input, train, training, sets, testing
+    href: how-to-guides/build-a-custom-model.md
+  - name: Build a custom classification model
+    displayName: custom, classifier, splitter
+    href: how-to-guides/build-a-custom-classifier.md
+  - name: Project sharing with custom models
+    displayName: project, share, sharing
+    href: how-to-guides/project-share-custom-models.md
+  - name: Compose custom extraction models
+    displayName: custom, models, modelId, model ID, train, dataset, data set, label, ocr, upload
+    href: how-to-guides/compose-custom-models.md
+  - name: Deploy the sample-labeling tool
+    displayName: FOTT, migration, containers, docker
+    href: v21/deploy-label-tool.md
+  - name: Train a custom model with the sample-labeling tool
+    displayName: FOTT, migration, containers, docker
+    href: v21/label-tool.md
+  - name: Use table tags to train your custom model
+    displayName: FOTT, migration, dynamic
+    href: v21/supervised-table-tags.md
+- name: Back up and recover models
+  displayName: disaster, recovery, region, copy, modelId, model ID
+  href: disaster-recovery.md
+- name: Configure secure communications
+  items:
+  - name: Set up Virtual Networks
+    displayName: firewall, security, subdomain, VNet, virtual network, az, regions, cli
+    href: ../../ai-services/cognitive-services-virtual-networks.md?context=/azure/ai-services/document-intelligence/context/context
+  - name: Create and use managed identities
+    displayName: azure RBAC, role based access control, sas, private, assigned, system assigned, role, blob
+    href: authentication/managed-identities.md
+  - name: Configure managed identities with private endpoints
+    displayName: Azure RBAC, role based access control, sas, private, assigned, system assigned, role, blob, virtual, firewalls, VNet, virtual networks, endpoints, storage
+    href: authentication/managed-identities-secured-access.md
+  - name: Use customer-managed keys
+    displayName: encrypt, encryption, key vault
+    href: authentication/encrypt-data-at-rest.md
+  - name: Use Microsoft Entra authentication
+    displayName: headers, subscription, access token, azure active directory, subdomain, role, service principal
+    href: ../../ai-services/authentication.md?context=/azure/ai-services/document-intelligence/context/context
+    
 - name: Containers
   items:
   - name: Install and run containers
@@ -306,12 +311,12 @@ items:
       href: /rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true
     - name: 2023-07-31 GA (v3.1)
       href: /rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP
-    - name: 2022-08-31 GA (v3.0)
+    - name: 2022-08-31 v3.0 (retires March 30, 2029)
       href: /rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP
+    - name: v2.1 (retires September 15, 2027)
+      href: /rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true
     - name: Error codes v4.0, v3.1, and v3.0
       href: how-to-guides/resolve-errors.md
-    - name: v2.1
-      href: /rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true
   - name: Client libraries (2024-11-30 GA)
     items:
     - name: C# / .NET
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント目次の更新と整理"
}
```

### Explanation
この変更は、`toc.yml`ファイルにおいて、ドキュメントの目次の大幅な更新と整理が行われたことを示しています。具体的には、追加された項目やカテゴリが57、削除された項目が52あり、合計で109の変更が行われました。

主な変更点には、移行ガイド関連の項目の再構成と、新しい情報の追加が含まれます。特に、Migration guidesというセクションが強調され、新たに「Migration guide overview」が設けられ、その中には.NET、Java、Python SDKに対する個別のマイグレーションガイドへのリンクが設置されています。また、Changelog（変更履歴）の表現も簡素化され、「SDK Migration guides」という名称が「Migration guides」に変更されています。

さらに、カスタムモデルに関連する項目が整理され、具体的にどのようにカスタム抽出モデルや分類モデルを構築できるかに関する詳細が提供されています。通信のセキュリティに関する項目や、コンテナ関連の設定方法も新しく追加され、利用者が必要な情報を見つけやすくなるように設計されています。

全体として、この変更はドキュメントの構造を改善し、情報の可視性を高めることを目的としています。

## articles/ai-services/document-intelligence/versioning/migration-guide-overview.md{#item-49f49c}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: "How-to: Migrate Document Intelligence applications to v3.1."
+title: "Migrate to v4.0."
 titleSuffix: Foundry Tools
 description: In this how-to guide, learn the differences between Document Intelligence API versions and how to move to the newer version of the API.
 author: laujan
@@ -12,11 +12,26 @@ monikerRange: '<=doc-intel-4.0.0'
 ---
 
 <!-- markdownlint-disable MD004 -->
+<!-- markdownlint-disable MD025 -->
 # Document Intelligence v4.0 migration
 
 > [!IMPORTANT]
 >
-> Document Intelligence REST API v4.0 introduces breaking changes in the REST API request and analyze response JSON.
+> * **Document Intelligence REST API v2.1** reaches end of support on **September 15, 2027**.
+> * **Document Intelligence REST API 2022-08-31 v3.0** reaches end of support on **March 30, 2029**.
+> * To avoid production disruption, use this migration guide to move to **Azure Document Intelligence 2024-11-30 v4.0**.
+
+## SDk migration guides
+
+For guidance on updating your application code to use the v4.0 SDKs, see the language-specific SDK migration guides in our GitHub repositories. These guides provide instructions for updating your code to call the new API methods and handle the updated response formats introduced in v4.0:
+
+* [**.NET/C# SDK**](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/documentintelligence/Azure.AI.DocumentIntelligence/MigrationGuide.md/)
+
+* [**Java SDK**](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/MIGRATION_GUIDE.md)
+
+* [**Python SDK**](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/MIGRATION_GUIDE.md)
+
+* [**JavaScript/TypeScript SDK**](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/documentintelligence/ai-document-intelligence-rest/MIGRATION-FR_v4-DI_v1.md)*
 
 ## Migrating from v3.1 to v4.0
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マイグレーションガイドの名称変更と内容の更新"
}
```

### Explanation
この変更では、`v3-1-migration-guide.md`ファイルが`migration-guide-overview.md`に名称変更され、内容が更新されました。主な目的は、Document Intelligence APIの新バージョンであるv4.0への移行プロセスを明確に示すことです。

ファイルの冒頭では、タイトルが「How-to: Migrate Document Intelligence applications to v3.1.」から「Migrate to v4.0.」に変更され、v4.0への移行に関連する情報が強調されています。新しいバージョンでは、古いAPIのサポート終了日が明示され、ユーザーが適時に移行を行うよう促されています。具体的には、v2.1は2027年9月15日に、v3.0は2029年3月30日にサポートが終了します。

さらに、SDKのマイグレーションガイドが言語ごとにリンクされており、それぞれのSDKに合わせた更新方法が説明されています。これにより、開発者は新しいAPIメソッドに呼び出しを変更し、v4.0で導入された更新されたレスポンスフォーマットを適切に扱うための具体的な手順を得ることができます。

全体として、この変更はAPIの移行プロセスを分かりやすくし、利用者が新しいバージョンにスムーズに移行できるようにすることを目的としています。

## articles/ai-services/document-intelligence/versioning/sdk-overview-v3-0.md{#item-f82845}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-document-intelligence
 ms.custom:
   - devx-track-python
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 05/06/2026
 ms.author: lajanuar
 monikerRange: 'doc-intel-3.0.0'
 ---
@@ -19,9 +19,14 @@ monikerRange: 'doc-intel-3.0.0'
 <!-- markdownlint-disable MD001 -->
 <!-- markdownlint-disable MD051 -->
 
-# SDK target: REST API 2022–08–31 (GA)
+# SDK target: REST API 2022–08–31 v3.0
 
-![Document Intelligence checkmark]../media/yes-icon.png) **REST API version 2022–08–31 (GA)**
+![Document Intelligence checkmark](../media/yes-icon.png) **REST API version 2022–08–31 v3.0**
+
+> [!IMPORTANT]
+>
+> * **Document Intelligence REST API 2022-08-31 v3.0** reaches end of support on **March 30, 2029**.
+> * To avoid production disruption, migrate now to **Azure Document Intelligence 2024-11-30 v4.0**. For more information, see [**Document Intelligence migration guide**](migration-guide-overview.md).
 
 Azure Document Intelligence in Foundry Tools is a cloud service that uses machine learning to analyze text and structured data from documents. The Document Intelligence software development kit (SDK) is a set of libraries and tools that enable you to easily integrate Document Intelligence models and capabilities into your applications. Document Intelligence SDK is available across platforms in C#/.NET, Java, JavaScript, and Python programming languages.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDK概要の更新とサポート期限の明示"
}
```

### Explanation
この変更では、`sdk-overview-v3-0.md`ファイルに対していくつかの重要な更新が行われました。主な改訂内容としては、ドキュメントインテリジェンスのSDKターゲットバージョンや、それに伴うサポート期限の情報が追加されています。

具体的には、APIのバージョン名が「REST API 2022–08–31 (GA)」から「REST API 2022–08–31 v3.0」に変更され、より明確な表現に改訂されています。また、重要な注意書きとして、「Document Intelligence REST API 2022-08-31 v3.0」のサポート終了日が2029年3月30日であることが追加され、さらに次のバージョンであるv4.0への早期移行を促す文言も含まれています。これにより、ユーザーがサポート期限を意識し、適切な対策を講じることが簡単になります。

また、メタデータに含まれる日付が2025年11月18日から2026年5月6日に更新され、最新の情報を反映した内容となっています。

全体として、この変更はSDKに関する重要な情報を更新し、利用者に対して適切な移行を促進する意図があると考えられます。

## articles/ai-services/document-intelligence/versioning/sdk-overview-v4-0.md{#item-d59a82}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - devx-track-js
   - devx-track-python
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 05/06/2026
 ms.author: lajanuar
 monikerRange: 'doc-intel-4.0.0'
 --- 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDK概要の更新日付の変更"
}
```

### Explanation
この変更では、`sdk-overview-v4-0.md`ファイルのメタデータに含まれる更新日付が変更されています。具体的には、日付が「2025年11月18日」から「2026年5月6日」に変更されました。この更新は、文書の最新性を反映させるためのものであり、ドキュメントが新しい情報に基づいていることを示しています。

他の内容に大きな変更はありませんが、日付の更新は、ユーザーにとって重要な情報であり、内容の信頼性や関連性を確保する上で必須です。この変更により、利用者はドキュメントが最近のものであると認識し、その内容に基づいて適切な判断を行いやすくなります。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -25,16 +25,17 @@ ms.custom:
 Document Intelligence service is updated on an ongoing basis. Bookmark this page to stay up to date with release notes, feature enhancements, and our newest documentation.
 
 > [!IMPORTANT]
-> Preview API versions will be retired by 06/30/2026, and v3.0 `2022-08-31 (GA)` API will be retired by 03/30/2029. If you're still using a preview API or the associated SDK versions, update your code to target the latest API version `2024-11-30 (GA)`. </br>
-
+>
+> * **Document Intelligence REST API v2.1** reaches end of support on **September 15, 2027**.
+> * **Document Intelligence REST API 2022-08-31 v3.0** reaches end of support on **March 30, 2029**.
+> * To avoid production disruption, migrate now to **Azure Document Intelligence 2024-11-30 v4.0**. For more information, see [**Document Intelligence migration guide**](versioning/migration-guide-overview.md).
 
 ## March 2026
 
 **Updated prebuilt tax form models**
 
 Prebuilt models for US tax forms have been updated supporting 2025 tax forms including quality improvement to address multi-copy extraction (e.g., multiple W-2s or 1099s in one document). You can now extract data from multi-form filings in a single request and get more comprehensive field coverage.
 
-
 ## June 2025
 
 **Document Intelligence v4.0 Read container is now available!**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "機能更新とサポート終了情報の追加"
}
```

### Explanation
この変更では、`whats-new.md`ファイルに新しい機能やサポート終了予定についての情報が追加されています。具体的には、ドキュメントインテリジェンスのREST APIに関する重要なスケジュールが更新されました。

新たに次の情報が追加されています：
- **Document Intelligence REST API v2.1** のサポート終了予定日が **2027年9月15日** であること。
- **Document Intelligence REST API 2022-08-31 v3.0** のサポート終了予定日が **2029年3月30日** であること。
- これに伴い、最新のAPIバージョンである **Azure Document Intelligence 2024-11-30 v4.0** への移行を求める文言も追加され、詳細については「**Document Intelligence migration guide**」へのリンクが提供されています。

また、過去の更新情報として、2026年3月に米国の税務関連の事前構築モデルが更新され、特に複数コピーの抽出に関する改善がなされた旨が記載されています。

全体として、この変更はユーザーにとって重要な案内であり、サービスの利用や更新に関する正確な情報を提供することを目的としています。ユーザーはこれにより、使用しているAPIやSDKのサポート状況を把握し、必要な対策を講じることができます。


