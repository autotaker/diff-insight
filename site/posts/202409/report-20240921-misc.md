---
date: '2024-09-21'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:daa818e...MicrosoftDocs:bb3e91f
summary: この差分の主な変更点は、RBAC関連文書の注意事項削除、Quota管理手順の簡略化、複数の画像削除、トピック名の変更（AI StudioとAzure
  Machine Learning Studio）です。新機能の追加はありませんが、既存の内容が整理され、わかりやすい形に改編されています。RBACに関する注意事項の削除は、以前のカスタムロール作成に必要な情報が省かれ、Quota管理の詳細手順や画像の削除により、ユーザーが旧情報に混乱する可能性があります。また、特定のトピック名称の変更により、情報提供がより明確になりました。全体として、これらの変更はAzure
  AI Studioのドキュメントをユーザーにとって分かりやすくし、必要な情報へのアクセスを容易にすることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:daa818e...MicrosoftDocs:bb3e91f){target="_blank"}

# ハイライト
この差分の主な変更点は以下の通りです：

- RBAC関連文書での注意事項削除
- Quota管理手順の簡略化
- 複数の画像（クォータに関する）の削除
- 関連トピック名の変更（AI StudioとAzure Machine Learning Studio）

## 新機能
特に新たな機能の追加はありませんが、既存の内容が整理され、利用者にとってわかりやすい形で改編されています。

## 破壊的変更
- RBACに関する注意事項の削除により、以前カスタムロール作成時に必要だった情報が削除されました。
- Quota管理に関する詳細手順や特定の画像が削除され、旧情報に依存したユーザーは戸惑う可能性があります。

## その他の更新
- toc.ymlの特定のトピック名称変更により、よりユーザーフレンドリーで明確な情報提供がなされました。

# インサイト
このコード差分では、主にドキュメントの整理とユーザーエクスペリエンス（UX）の向上が図られています。RBACに関する注意事項削除は、不要な情報を省くことで、カスタムロール作成に関する流れをスムーズにしています。これにより、ユーザーがより本質的な情報に集中できるようになっています。

Quota管理手順の簡略化および画像の削除は、Azure AI Studio内での操作フローを効率化するための措置と思われます。特に、詳細な手順が削除されたことにより、一般的なQuota管理に関する情報が強調され、手順が簡潔かつ明確になりました。

画像の削除は、最新の情報に基づいた内容が反映された結果であり、文書の整合性および読みやすさが向上しています。これにより、利用者は不要なビジュアル要素による混乱が減り、より迅速に必要な情報を得ることができます。

さらに、「AI Studio or Azure Machine Learning Studio: Which should I choose?」という新しいトピック名ですが、これはユーザーがどちらのスタジオを選択すべきかをもっと具体的に考える上で有用です。以前のトピック名よりもはるかに情報が明確になり、ユーザーの関心を引きやすい構造に変更されています。

総じて、これらの変更は、Azure AI Studioのドキュメントがユーザーにとってわかりやすく、必要な情報にアクセスしやすいものとなるように設計されています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [rbac-ai-studio.md](#item-c2a11a) | minor update | RBACに関する注意事項の削除 | modified | 0 | 3 | 3 | 
| [quota.md](#item-39c866) | minor update | Quota管理の手順の簡略化 | modified | 4 | 16 | 20 | 
| [model-quota.png](#item-d9eb98) | minor update | モデルクォータ画像の削除 | removed | 0 | 0 | 0 | 
| [select-model-vm-quota.png](#item-476b34) | minor update | モデルおよびVMクォータ選択画像の削除 | removed | 0 | 0 | 0 | 
| [vm-quota.png](#item-34af5c) | minor update | VMクォータ画像の削除 | removed | 0 | 0 | 0 | 
| [toc.yml](#item-2745cd) | minor update | AI StudioとAML Studioの項目名の変更 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-studio/concepts/rbac-ai-studio.md{#item-c2a11a}

<details>
<summary>Diff</summary>
````diff
@@ -144,9 +144,6 @@ az role assignment create --role "Azure AI Developer" --assignee "joe@contoso.co
 
 ## Create custom roles
 
-> [!NOTE]
-> In order to make a new hub, you need the Owner or Contributor role. At this time, a custom role, even with all actions allowed, will not enable you to make a hub. 
-
 If the built-in roles are insufficient, you can create custom roles. Custom roles might have the read, write, delete, and compute resource permissions in that AI Studio. You can make the role available at a specific project level, a specific resource group level, or a specific subscription level. 
 
 > [!NOTE]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACに関する注意事項の削除"
}
```

### Explanation
このコードの差分は、`rbac-ai-studio.md`ファイルに対する軽微な更新を示しています。具体的には、3行のテキストが削除されています。削除された内容は、カスタムロールを作成する際の注意事項に関するもので、「新しいハブを作成するには、オーナーまたは貢献者の役割が必要」といった点が含まれていました。この変更により、役割に関連する情報が簡潔になり、ユーザーがカスタムロール作成時に必要な情報によりフォーカスできるようになっています。詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/raw/bb3e91fad42d16a636e7c386fe17d9f1e52b80c2/articles%2Fai-studio%2Fconcepts%2Frbac-ai-studio.md)から確認できます。

## articles/ai-studio/how-to/quota.md{#item-39c866}

<details>
<summary>Diff</summary>
````diff
@@ -93,25 +93,13 @@ Azure Storage has a limit of 250 storage accounts per region, per subscription.
 
 Use quotas to manage compute target allocation between multiple Azure AI Studio hubs in the same subscription. 
 
-By default, all hubs share the same quota as the subscription-level quota for VM families. However, you can set a maximum quota for individual VM families for more granular cost control and governance on hubs in a subscription. Quotas for individual VM families let you share capacity and avoid resource contention issues.
+By default, all hubs share the same quota as the subscription-level quota for VM families. However, you can set a maximum quota for individual VM families for more granular cost control and governance on hubs in a subscription. Quotas for individual VM families let you share capacity and avoid resource contention issues. 
 
-1. In Azure AI Studio, go to the **Home** page and select either **Model quota** or **VM quota** from the **Management** section.
+1. In Azure AI Studio, go to the **Home** page and select **Quota**. 
 
-    :::image type="content" source="../media/cost-management/select-model-vm-quota.png" alt-text="Screenshot of the Model and VM quota entries in the management section." lightbox="../media/cost-management/select-model-vm-quota.png":::
+1. Select the **Azure ML** tab to view the quota for the VM families. The quota is displayed at the subscription level in the selected Azure region. To request more quota, select the VM family and then select **Request quota**. 
 
-1. When you select **Model quota**, you can view the quota for the models in the selected Azure region. To request more quota, select the model and then select **Request quota**. 
-
-    - Use the **Show all quota** toggle to display all quota or only the currently allocated quota.
-    - Use the **Group by** dropdown to group the list by **Quota type, Region & Model**, **Quota type, Model & Region**, or **None**. The **None** grouping displays a list of model deployments.
-    - Expand the groupings to view information on specific model deployments. While viewing a model deployment, select the **pencil icon** in the **Quota allocation** column to edit the quota allocation for the model deployment.
-    - Use the **charts** along the side of the page to view more details about quota usage. The charts are interactive; hovering over a section of the chart displays more information, and selecting the chart filters the list of models. Selecting the chart legend filters the data displayed in the chart.
-    - Use the **Azure OpenAI Provisioned** link to view information about provisioned models, including a **Capacity calculator**.
-  
-    :::image type="content" source="../media/cost-management/model-quota.png" alt-text="Screenshot of the Model quota page in Azure AI Studio." lightbox="../media/cost-management/model-quota.png":::
-
-1. When you select **VM quota**, you can view the quota and usage for the virtual machine families in the selected Azure region. To request more quota, select the VM family and then select **Request quota**. 
-
-    :::image type="content" source="../media/cost-management/vm-quota.png" alt-text="Screenshot of the VM quota page in Azure AI Studio." lightbox="../media/cost-management/vm-quota.png":::
+    :::image type="content" source="../media/cost-management/quota-manage.png" alt-text="Screenshot of the page to view and request quota for VM families in Azure AI Studio." lightbox="../media/cost-management/quota-manage.png":::
 
 ## Next steps 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Quota管理の手順の簡略化"
}
```

### Explanation
このコードの差分は、`quota.md`ファイルに対する軽微な更新を示しています。全体として16行が削除され、4行が追加される形で20行の変更が行われました。主な変更点は、Quota管理の手順が簡略化されていることです。具体的には、Azure AI Studioでの操作手順が整理され、より効率的にQuotaを確認・リクエストできるようになっています。

特に、特定のモデルやVMのQuotaに関する詳細な手順が削除されており、代わりに一般のQuota管理に関する情報が強調されています。また、画像のリンクも更新され、新しい情報が反映されています。この変更により、利用者は手順をより迅速に理解しやすくなっています。詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/raw/bb3e91fad42d16a636e7c386fe17d9f1e52b80c2/articles%2Fai-studio%2Fhow-to%2Fquota.md)から確認できます。

## articles/ai-studio/media/cost-management/model-quota.png{#item-d9eb98}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルクォータ画像の削除"
}
```

### Explanation
このコードの差分は、`model-quota.png`という画像ファイルが削除されたことを示しています。この変更は、特定の画像がコスト管理に関する文書内で使用されなくなったことを反映しています。画像の削除により、もしかすると関連する内容が現在のドキュメントには不要であるか、もしくは他の画像と置き換わった可能性があります。

この変更によって、ドキュメントは最新の情報として整理され、利用者にとって不要な要素が除外された形になります。詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/raw/daa818e03b7d52048132a72936179cff4f5ee12b/articles%2Fai-studio%2Fmedia%2Fcost-management%2Fmodel-quota.png)から確認できます。

## articles/ai-studio/media/cost-management/select-model-vm-quota.png{#item-476b34}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルおよびVMクォータ選択画像の削除"
}
```

### Explanation
このコードの差分は、`select-model-vm-quota.png`という画像ファイルが削除されたことを示しています。この変更は、コスト管理に関連する文書内でこの特定の画像が不要とされたことを反映しています。画像の削除により、文書が最新の内容に更新された可能性があります。

削除された画像は、おそらくモデルと仮想マシンのクォータ選択に関する視覚的な情報を提供していましたが、利用者にとって無用になったか、他の方法で情報を伝える手段が採られた可能性があります。この更新により、文書はよりシンプルで読みやすくなり、最新情報に基づいた内容となります。詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/raw/daa818e03b7d52048132a72936179cff4f5ee12b/articles%2Fai-studio%2Fmedia%2Fcost-management%2Fselect-model-vm-quota.png)から確認できます。

## articles/ai-studio/media/cost-management/vm-quota.png{#item-34af5c}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "VMクォータ画像の削除"
}
```

### Explanation
このコードの差分は、`vm-quota.png`という画像ファイルが削除されたことを示しています。この変更は、コスト管理に関連するドキュメント内でこの特定の画像が不要とされたことを反映しています。画像の削除により、ドキュメントが最新の情報や使用状況の変化に適応している可能性があります。

削除された画像は、仮想マシンのクォータに関する視覚的な情報を提供していましたが、現在は他の資料や説明文によって十分にカバーされているか、もしくは情報が古くなったことが考えられます。この変更により、文書の整合性が保たれ、ユーザーにとってより理解しやすい内容になっています。詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/raw/daa818e03b7d52048132a72936179cff4f5ee12b/articles%2Fai-studio%2Fmedia%2Fcost-management%2Fvm-quota.png)から確認できます。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ items:
     href: what-is-ai-studio.md
   - name: Azure AI Studio architecture
     href: concepts/architecture.md
-  - name: AI Studio versus AML studio
+  - name: "AI Studio or Azure Machine Learning Studio: Which should I choose?"
     href: /ai/ai-studio-experiences-overview?context=/azure/ai-studio/context/context
   - name: Region support
     href: reference/region-support.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI StudioとAML Studioの項目名の変更"
}
```

### Explanation
このコードの差分は、`toc.yml`ファイルの内容が変更されたことを示しています。具体的には、AI Studioに関連するトピックの名称が変更されました。以前の項目名「AI Studio versus AML studio」は、新しい項目名「AI Studio or Azure Machine Learning Studio: Which should I choose?」に更新されました。この変更は、ユーザーが情報をより明確に理解できるようにするためのものであり、選択肢を提示する形で内容を充実させています。

この小さな更新は、特にユーザーがAI StudioとAzure Machine Learning Studioのどちらを選ぶべきかを考える際に役立ちます。更新された項目名は、文脈を明確にし、比較の具体的な焦点を示すことで、読者の関心を引きやすくします。詳細は、[こちらのリンク](https://github.com/MicrosoftDocs/azure-ai-docs/raw/bb3e91fad42d16a636e7c386fe17d9f1e52b80c2/articles%2Fai-studio%2Ftoc.yml)から確認できます。


